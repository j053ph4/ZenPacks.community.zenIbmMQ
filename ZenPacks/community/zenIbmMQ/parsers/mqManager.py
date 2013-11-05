import logging
log = logging.getLogger('zen.zenhub')

from Products.ZenRRD.CommandParser import CommandParser
from ZenPacks.community.zenIbmMQ.MQHandler import MQHandler

class mqManager(CommandParser):
    """
    """
    def getStatus(self,status):
        if 'Running' in status:
            return 1
        else:
            return 0
    
    def processResults(self, cmd, result):
        log.debug("processing cmd:%s result: %s" % (cmd,result))
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        parser = MQHandler(cmd.result.output.splitlines())
        parser.dataMap()
        log.debug("parser dict:%s" % parser.info)
        self.data = {}
        value = self.getStatus(output['STATUS'])
        self.data['status'] = value
        for d in self.data.items():
            try:
                result.values.append( (datapointMap[d[0]], long(d[1])) )
            except:
                pass
        log.debug("result: %s" % result)
        return result

