from Products.ZenRRD.CommandParser import CommandParser
from ZenPacks.community.zenIbmMQ.lib.MQHandler import *
import logging
log = logging.getLogger('zen.zenhub')

class mqChannel(CommandParser):
    ''''''
    def insertValue(self,key,value):
        ''''''
        try: self.data[key] = self.parser.info[value]
        except: self.data[key] = None
    
    def processResults(self, cmd, result):
        ''''''
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        self.parser = MQHandler(cmd.result.output.splitlines())
        self.parser.dataMap()
        #log.debug("parser dict:%s" % self.parser.info)
        self.data = {
                     'messages': None,
                     'bytesRcvd': None,
                     'bytesSent': None,
                     'buffersRcvd': None,
                     'buffersSent': None,
                     }
        self.insertValue('messages','MSGS')
        self.insertValue('bytesRcvd','BYTSRCVD')
        self.insertValue('bytesSent','BYTSSENT')
        self.insertValue('buffersRcvd','BUFSRCVD')
        self.insertValue('buffersSent','BUFSSENT')
        
        for d in self.data.items():
            try: result.values.append( (datapointMap[d[0]], long(d[1])) )
            except: pass
        #log.debug("result: %s" % result)
        return result

