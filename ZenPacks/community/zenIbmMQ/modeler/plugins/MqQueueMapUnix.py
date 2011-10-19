######################################################################
#
# MQ Manager Unix modeler plugin
#
######################################################################
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from ZenPacks.community.zenIbmMQ.modeler.plugins.Common import *

class MqQueueMapUnix(MQComponentMap,CommandPlugin):
    """
    """
    relname = "mqQueues"
    modname = "ZenPacks.community.zenIbmMQ.MQQueue"

    command = "for LINE in $(dspmq|awk '{print $1}'); " +\
            "do MGR=$(echo $LINE | cut -f 2 -d '(' | cut -f 1 -d ')');"+\
            "printf \"QueueManager ${MGR}\n\";"+\
            "echo 'DISPLAY QUEUE(*) ALL' | su - mqm -c \"runmqsc $MGR\" ; done"

    MQComponentMap.bundleKey = "QUEUE"

    deviceProperties = MQComponentMap.deviceProperties + CommandPlugin.deviceProperties


