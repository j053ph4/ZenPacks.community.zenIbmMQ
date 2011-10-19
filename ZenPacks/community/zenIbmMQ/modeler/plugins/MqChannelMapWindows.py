######################################################################
#
# MQ Manager Windows modeler plugin
#
######################################################################
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from ZenPacks.community.zenIbmMQ.modeler.plugins.Common import *

class MqChannelMapWindows(MQComponentMap,PythonPlugin):
    """
    """
    
    relname = "mqChannels"
    modname = "ZenPacks.community.zenIbmMQ.MQChannel"
    transport = "python"
    
    deviceProperties = MQComponentMap.deviceProperties + PythonPlugin.deviceProperties+ (
                'zWinUser',
                'zWinPassword',
                )
        
    def collect(self, device, log):
        winCommon = WindowsCommon()
        winCommon.connectInit(device.id,device.zWinUser,device.zWinPassword)
        return "CHANNEL",winCommon.getManagers()

        
