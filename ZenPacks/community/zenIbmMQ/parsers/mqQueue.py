import logging
log = logging.getLogger('zen.zenhub')

from Products.ZenRRD.CommandParser import CommandParser
from ZenPacks.community.zenIbmMQ.MQHandler import MQHandler

class mqQueue(CommandParser):
    """
    """
    def insertValue(self,key,value):
        try:
            self.data[key] = self.parser.info[value]
        except:
            pass
    
    def processResults(self, cmd, result):
        #log.info("processing cmd:%s result: %s" % (cmd,result))
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        parser = MQHandler(cmd.result.output.splitlines())
        parser.dataMap()
        log.debug("parser dict:%s" % parser.info)
        self.data = {}
        self.data['currDepth'] = 0
        self.data['trigDepth'] = 0
        self.data['ipProcs'] = 0
        self.data['opProcs'] = 0
        self.insertValue('currDepth','CURDEPTH')
        self.insertValue('trigDepth','TRIGDPTH')
        self.insertValue('ipProcs','IPPROCS')
        self.insertValue('opProcs','OPPROCS')
        for d in self.data.items():
            try:
                result.values.append( (datapointMap[d[0]], long(d[1])) )
            except:
                pass
        log.debug("result: %s" % result)
        return result
