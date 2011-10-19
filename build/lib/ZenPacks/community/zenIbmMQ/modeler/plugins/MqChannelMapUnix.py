######################################################################
#
# MQ Manager Unix modeler plugin
#
######################################################################
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from ZenPacks.community.zenIbmMQ.modeler.plugins.Common import *

class MqChannelMapUnix(MQComponentMap,CommandPlugin):
    """
    """
    relname = "mqChannels"
    modname = "ZenPacks.community.zenIbmMQ.MQChannel"
    
    deviceProperties = MQComponentMap.deviceProperties + CommandPlugin.deviceProperties

    MQComponentMap.bundleKey = "CHANNEL"
    
    command = "for LINE in $(dspmq|awk '{print $1}'); " +\
            "do MGR=$(echo $LINE | cut -f 2 -d '(' | cut -f 1 -d ')');"+\
            "printf \"QueueManager ${MGR}\n\";"+\
            "echo 'DISPLAY CHSTATUS(*) ALL' | su - mqm -c \"runmqsc $MGR\" ; done"  

