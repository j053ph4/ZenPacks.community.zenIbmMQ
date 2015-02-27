import re,os
from Products.ZenUtils.Utils import prepId
from Products.DataCollector.plugins.CollectorPlugin import *
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.zenIbmMQ.lib.MQHandler import *
from subprocess import *

class MQComponentMap(CommandPlugin):
    """
    """
    transport = "command"
    command = ""
    deviceProperties = CommandPlugin.deviceProperties + (
                            'zWinUser',
                            'zWinPassword',
                            'zMqRunsOnUnix',
                            'zMqUsername',
                            )
    bundleKey = ""
    baseid = ''
    
    def collect(self, device, log):
        '''
            method used with python transport
        '''
        log.info("collecting %s for %s." % (self.name(), device.id))
        if str(device.zMqRunsOnUnix) == "True":
            collect = MQCollect('unix')
            collect.connect(device.manageIp, device.zCommandUsername, device.zCommandPassword) 
        else:
            collect = MQCollect('windows')
            collect.connect(device.id, device.zWinUser, device.zWinPassword)
        items = collect.collect('manager')
        data = {}
        for item in items:
            try: manager = item['QMNAME']
            except: continue
            status = item['STATUS']
            #log.debug('found manager: %s status: %s' % (manager,status))
            data[manager] = {'status': status,'items': []}
            if self.bundleKey == 'QUEUE': data[manager]['items'] = collect.collect('queue', manager)
            if self.bundleKey == 'CHANNEL': data[manager]['items'] = collect.collect('channel', manager)
            if self.bundleKey == 'QMNAME': 
                data[manager]['items'] = collect.collect('manager')
                return data
        return data
    
    def process(self, device, results, log):
        """ adds Zenoss components based on given list of dictionaries
        """
        log.info("The plugin %s returned %s results." % (self.name(), len(results)))
        common = MQCommon(self.baseid)
        objects = common.parseResults(self.bundleKey,results)
        rm = self.relMap()
        for o in objects:
            om = self.objectMap(o)
            om.monitor = o['monitor']
            if self.modname == 'MQManager':
                om.setOsprocess = ''
            else:
                om.setMqmanager = o['manager']
            log.debug(om)
            rm.append(om)
        return rm
    
    def preprocess(self,results,log):
        ''''''
        return results

class MQCollect():
    def __init__(self, remote='unix'):
        self.remote = remote
    
    def connect(self, device, user, password):
        self.nixcmd = "sshpass -p %s ssh -o StrictHostKeyChecking=no %s@%s '%s'" % (password, user, device,'%s')
        self.wincmd = '/opt/zenoss/bin/winexe -U "%s" "%s" ' % (user+'%%'+password, '//%s' % device)
        self.commands = {
                     'manager':{
                            'key' : 'QMNAME',
                            'unix': self.nixcmd % 'su - mqm -c "dspmq"' ,
                            'windows': 'echo | %s "dspmq"' % self.wincmd
                            },
                     'queue':{
                            'key' : 'QUEUE',
                            'unix': self.nixcmd %  '''/bin/echo DISPLAY QUEUE\(*\) ALL | su - mqm -c "runmqsc %s"''',
                            'windows': '/usr/bin/printf "DISPLAY QUEUE(*) ALL\nEND\n" | %s "runmqsc %s"' % (self.wincmd,"%s")
                            },
                     'channel':{
                            'key' : 'CHANNEL',
                            'unix': self.nixcmd % '''/bin/echo DISPLAY CHANNEL\(*\) ALL | su - mqm -c "runmqsc %s"''',
                            'windows': '/usr/bin/printf "DISPLAY CHSTATUS(*) ALL\nEND\n" | %s "runmqsc %s"' % (self.wincmd,"%s")
                            },
                     }
    
    def collect(self, query, manager=None):
        command = self.commands[query][self.remote]
        if manager:
            command = command % manager            
        command = command.replace('%%','%')
        #print "COMMAND: %s" % command
        output = Popen([command],stdout=PIPE,shell=True)
        result = output.stdout.read()
        handler = MQHandler(result.splitlines())
        return handler.parseData(self.commands[query]['key'])

class MQCommon():
    """ 
    """
    def __init__(self,baseid):
        """
        """
        self.baseid = baseid
    
    def getStatus(self, status):
        if 'Running' in status:  
            return True
        else: return False
    
    def parseResults(self, bundleKey, dataDict):
        objects = []
        ignoreKeys = ['SYSTEM', 'COM.IBM.MQ.PCF']
        for manager, data in dataDict.items():
            status = data['status']
            items = data['items']
            for item in items:
                if bundleKey == 'QMNAME':
                    name = item['QMNAME']
                    ob = self.ManagerInfo(item)
                elif bundleKey == 'QUEUE':
                    name = item['QUEUE']
                    ob = self.QueueInfo(manager, item)
                    ob['monitor'] = self.getStatus(status)
                else:
                    name = item['CHANNEL']
                    ob = self.ChannelInfo(manager, item)
                    ob['monitor'] = self.getStatus(status)
                skip = False
                for i in ignoreKeys:
                    if i in name: 
                        #log.debug("skipping %s" % name)
                        skip = True
                if skip is True: continue
                objects.append(ob)
        return objects
    
    def ManagerInfo(self,dataDict):
        """ Map MQ data to component attributes """
        name = "%s_%s" % (self.baseid, dataDict['QMNAME'])
        info = {'id' : prepId(name), 'managerName' : dataDict['QMNAME'], 'managerStatus': dataDict['STATUS'],}
        info['monitor'] = self.getStatus(dataDict['STATUS'])
        info['manager'] = dataDict['QMNAME']
        return info
    
    def QueueInfo(self,manager,dataDict):
        """ Map MQ data to component attributes """
        keyMap = {'QUEUE': 'queueName','TYPE': 'queueType', 'MAXDEPTH': 'queueMaxDepth'}
        name = "%s_%s_%s" % (self.baseid, dataDict['QUEUE'], manager)
        name = re.sub('[^A-Za-z0-9]+', '_', name)
        info = {'id':prepId(name), 'queueManager': manager,}
        for k,v in keyMap.items():
            try: info[v] = dataDict[k]
            except: info[v] = ''
        if info['queueType'] == 'QREMOTE': info['monitor'] = False
        info['manager'] = manager
        return info
    
    def ChannelInfo(self,manager,dataDict):
        """ Map MQ data to component attributes """
        keyMap = {'CHANNEL': 'channelName','CONNAME': 'channelConn', 'CHLTYPE': 'channelType', 'STATUS': 'channelStatus' }
        try: name = "%s_%s_%s_%s_%s" % (self.baseid, dataDict['CHANNEL'], manager, dataDict['CONNAME'], dataDict['CHLTYPE'])
        except: name = "%s_%s_%s_%s" % (self.baseid, dataDict['CHANNEL'], manager, dataDict['CHLTYPE'])
        name = re.sub('[^A-Za-z0-9]+', '_', name)
        info = {'id':prepId(name), 'channelManager': manager}
        for k,v in keyMap.items():
            try: info[v] = dataDict[k]
            except: info[v] = ''
        info['manager'] = manager
        return info

