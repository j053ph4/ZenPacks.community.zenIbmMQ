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

class mqManager(CommandParser):
    """
    """

    def getStatus(self,status):
        if status == 'Running':
            return 1
        else:
            return 0
    
    def processResults(self, cmd, result):
        
        datapointMap = dict([(dp.id, dp) for dp in cmd.points])
        self.parser = MQParser()
        self.parser.lines = cmd.result.output.replace('\r\n','\n').splitlines()
        self.parser.dataMap()
        self.data = {}
        value = self.getStatus(self.parser.info['STATUS'])
        self.data['status'] = value

        for d in self.data.items():
            try:
                result.values.append( (datapointMap[d[0]], long(d[1])) )
            except:
                pass
        return result

