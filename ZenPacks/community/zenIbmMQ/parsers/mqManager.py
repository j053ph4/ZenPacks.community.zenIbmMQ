from Products.ZenRRD.CommandParser import CommandParser
from ZenPacks.community.zenIbmMQ.lib.MQHandler import *
import logging
log = logging.getLogger('zen.zenhub')



class mqManager(CommandParser):
    ''''''
    managerRunStateMap = {
               4: 'Running',
               3: 'Online',
               2: 'Unavailable',
               1: 'Stopped',
               0: 'Shutdown',
               -1: 'Unknown',
               }
    
    def getStatus(self, status):
        for value, state in self.managerRunStateMap.items():
                if state in status: return value
        #if 'Running' in status: return 1
        return -1
    
    def processResults(self, cmd, result):
        #log.debug("processing cmd:%s result: %s" % (cmd,result))
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        parser = MQHandler(cmd.result.output.splitlines())
        parser.dataMap()
        #log.debug("parser dict:%s" % parser.info)
        self.data = {}
        value = 0
        try: value = self.getStatus(parser.info['STATUS'])
        except: pass
        self.data['status'] = value
        for d in self.data.items():
            try: result.values.append( (datapointMap[d[0]], long(d[1])) )
            except: pass
        #log.debug("result: %s" % result)
        return result

