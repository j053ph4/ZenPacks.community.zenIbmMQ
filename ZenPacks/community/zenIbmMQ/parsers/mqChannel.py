import logging
log = logging.getLogger('zen.zenhub')

from Products.ZenRRD.CommandParser import CommandParser
from ZenPacks.community.zenIbmMQ.MQHandler import MQHandler

class mqChannel(CommandParser):
    """
    """
    
    def insertValue(self,key,value):
        try:
            self.data[key] = self.parser.info[value]
        except:
            pass
    
    def processResults(self, cmd, result):
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        parser = MQHandler(cmd.result.output.splitlines())
        parser.dataMap()
        log.debug("parser dict:%s" % parser.info)
        self.data = {}
        self.data['messages'] = None
        self.data['bytesRcvd'] = None
        self.data['bytesSent'] = None
        self.data['buffersRcvd'] = None
        self.data['buffersSent'] = None
        
        self.insertValue('messages','MSGS')
        self.insertValue('bytesRcvd','BYTSRCVD')
        self.insertValue('bytesSent','BYTSSENT')
        self.insertValue('buffersRcvd','BUFSRCVD')
        self.insertValue('buffersSent','BUFSSENT')
        
        for d in self.data.items():
            try:
                result.values.append( (datapointMap[d[0]], long(d[1])) )
            except:
                pass
        log.debug("result: %s" % result)
        return result

