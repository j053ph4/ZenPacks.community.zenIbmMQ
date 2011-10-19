###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2008, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

from Products.ZenRRD.CommandParser import CommandParser
from ZenPacks.community.zenIbmMQ.MQHandler import MQParser

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
        self.parser = MQParser()
        self.parser.lines = cmd.result.output.replace('\r\n','\n').splitlines()
        self.parser.dataMap()
        
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
        return result

