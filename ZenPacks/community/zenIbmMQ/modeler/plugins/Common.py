import re,os
from Products.ZenUtils.Utils import prepId
from Products.DataCollector.plugins.CollectorPlugin import CollectorPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.zenIbmMQ.MQHandler import MQParser
from subprocess import *

class MQComponentMap():
    """
    """
    deviceProperties = (
                'zMqRunsOnUnix',
                )

    def findUnixBundleKey(self,input):
        """  correct a bug with the class inheritance
        """
        for line in input.split('\n'):
            if re.search('CHANNEL',line) != None:
                self.bundleKey = 'CHANNEL'
                break
            if re.search('QUEUE',line) != None:
                self.bundleKey = 'QUEUE'
                break
            if re.search('QMNAME',line) != None:
                self.bundleKey = 'QMNAME'
                break

    def process(self, device, results, log):
        """ adds Zenoss components based on given list of dictionaries
        """
        log.info('Collecting MQ components for device %s' % device.id)
        
        common = Common()
        dataDict = {}
        if device.zMqRunsOnUnix == True:
            self.findUnixBundleKey(results)
            dataDict = common.unixDictionary(results)
        else:
            self.bundleKey,output = results
            dataDict = common.windowsDictionary(output,device.id,device.zWinUser,device.zWinPassword,self.bundleKey)

        objects = common.parseResults(self.bundleKey,dataDict)
        rm = self.relMap()
        log.info('Found %s components of type %s' %(len(objects),self.bundleKey))
        for o in objects:
            om = self.objectMap(o)
            rm.append(om)
        return rm
    
    
class Common():
    """ 
    """
    def __init__(self):
        """
        """
        self.parser = MQParser()
        self.wincommon = WindowsCommon()
        
    def ManagerInfo(self,dataDict):
        """ Map MQ data to component attributes
        """
        info = {}
        name = dataDict['QMNAME']
        info['id'] = prepId(name)
        info['managerName'] = name
        info['managerStatus'] = dataDict['STATUS']
        return info
    
    def QueueInfo(self,manager,dataDict):
        """ Map MQ data to component attributes
        """
        info = {}
        name = dataDict['QUEUE']
        info['id'] = prepId(name)
        info['queueName'] = name
        info['queueManager'] = manager
        info['queueType'] = dataDict['TYPE']
        info['queueMaxDepth'] = dataDict['MAXDEPTH']
        return info
    
    def ChannelInfo(self,manager,dataDict):
        """ Map MQ data to component attributes
        """
        info = {}
        name = dataDict['CHANNEL']
        info['id'] = prepId(name)
        info['channelName'] = name
        info['channelConn'] = dataDict['CONNAME']
        info['channelType'] = dataDict['CHLTYPE']
        info['channelStatus'] = dataDict['STATUS']
        info['channelManager'] = manager
        return info
    
    def parseBundle(self,manager,bundles,bundleKey):
        """ return dictionary objects for components
        """
        output = []
        for bundle in bundles:
            self.parser.lines = bundle
            self.parser.dataMap()
            try:
                test = self.parser.info[bundleKey]
                if re.search('CHANNEL',bundleKey) != None:
                    if re.search('SYSTEM',test) == None:
                        output.append(self.ChannelInfo(manager,self.parser.info))
                elif re.search('QUEUE',bundleKey) != None:
                    if re.search('SYSTEM',test) != None:
                        pass
                    elif re.search('COM.IBM.MQ.PCF',test) != None:
                        pass
                    else:
                        output.append(self.QueueInfo(manager,self.parser.info))
                elif re.search('QMNAME',bundleKey) != None:
                    output.append(self.ManagerInfo(self.parser.info))
            except:
                pass
        return output
    
    def unixDictionary(self,input):
        """
        """
        dataDict = {}
        resultlines = input.split("\n")
        manager = ''
        addLine=False
        for line in resultlines:
            if re.search("QueueManager ",line) != None: # new manager
                manager = line[len("QueueManager "):len(line)]
                dataDict[manager] = []
                addLine=True
            elif re.search("QMNAME",line) != None: # parsing output of dspmq
                manager = line[line.find("(")+1:line.find(")")]
                dataDict[manager] = []
                line = re.sub(' +','  ',line)
                addLine=True
            if addLine == True:
                dataDict[manager].append(line)          
        return dataDict
    
    def windowsDictionary(self,input,device,user,password,bundleKey):
        """
        """
        dataDict = {}
        self.parser.lines = input
        for line in self.parser.cleanLines():
            key,value = self.parser.keyValue(line)
            if key == 'QMNAME': # name of queue manager
                manager = value
                dataDict[manager] = self.wincommon.getWindowsComponents(device,user,password,manager,bundleKey)
        return dataDict
    
    def parseResults(self,bundleKey,dataDict):
        """
        """
        beginString = "QueueManager "
        endString = "All valid MQSC commands were processed"
        midString = ''
        objects = []
        if re.search('CHANNEL',bundleKey) != None:
            midString = "AMQ8417"
        elif re.search('QUEUE',bundleKey) != None:
            midString = "AMQ8409"
        elif re.search('QMNAME',bundleKey) != None:
            for manager,list in dataDict.items():
                objects += self.parseBundle(manager,[list],bundleKey)
            return objects
        for manager,list in dataDict.items():
            bundles = self.parser.bundleData(list,beginString,midString,endString) 
            objects += self.parseBundle(manager,bundles,bundleKey)  
        return objects


class WindowsCommon():
    """
    """
    def __init__(self):
        """
        """
        self.winexe = '/opt/zenoss/bin/winexe'
        self.newline = '\r\n'
        
    def connectInit(self,device,user,password):
        self.authString = user+'%'+password
        self.destString = '//' + device
    
    def getManagers(self):
        """ retrieve list of queue managers
        """
        localCommand = 'echo | /opt/zenoss/bin/winexe -U "'+self.authString+'" '+self.destString+' "dspmq"'
        #print localCommand
        output = Popen([localCommand],stdout=PIPE,shell=True)
        return output.stdout.readlines()
    
    def getQueues(self,manager):
        """ retrieve list of mq channel data
        """
        localCommand = '/usr/bin/printf "DISPLAY QUEUE(*) ALL\nEND\n" |'+\
        '/opt/zenoss/bin/winexe -U "'+self.authString+'" '+self.destString+\
        ' "runmqsc '+manager+'"'
        output = Popen([localCommand],stdout=PIPE,shell=True)
        return output.stdout.readlines()
    
    def getChannels(self,manager):
        """ retrieve list of mq channel data
        """
        localCommand = '/usr/bin/printf "DISPLAY CHSTATUS(*) ALL\nEND\n" |'+\
        '/opt/zenoss/bin/winexe -U "'+self.authString+'" '+self.destString+\
        ' "runmqsc '+manager+'"'
        output = Popen([localCommand],stdout=PIPE,shell=True)
        return output.stdout.readlines()

    def getWindowsComponents(self,device,user,password,manager,bundleKey):
        """

        """
        output = []
        self.connectInit(device, user, password)
        if re.search('CHANNEL',bundleKey) != None:
            return self.getChannels(manager)
        elif re.search('QUEUE',bundleKey) != None:
            return self.getQueues(manager)
        elif re.search('QMNAME',bundleKey) != None:
            return self.getManagers()
    
