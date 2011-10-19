######################################################################
#
# MQ Manager Unix modeler plugin
#
######################################################################
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from ZenPacks.community.zenIbmMQ.modeler.plugins.Common import *

class MqManagerMapUnix(MQComponentMap,CommandPlugin):
    """
    """
    relname = "mqManagers"
    modname = "ZenPacks.community.zenIbmMQ.MQManager"
    
    deviceProperties = MQComponentMap.deviceProperties + CommandPlugin.deviceProperties
    
    MQComponentMap.bundleKey = "QMNAME"
    
    command = 'su - mqm -c dspmq'


