######################################################################
#
# MQ Manager Windows modeler plugin
#
######################################################################
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from ZenPacks.community.zenIbmMQ.modeler.plugins.Common import *

class MqManagerMapWindows(MQComponentMap,PythonPlugin):
    """
    """
    
    relname = "mqManagers"
    modname = "ZenPacks.community.zenIbmMQ.MQManager"
    transport = "python"
    
    deviceProperties = MQComponentMap.deviceProperties + PythonPlugin.deviceProperties+ (
                'zWinUser',
                'zWinPassword',
                )

    def collect(self, device, log):
        winCommon = WindowsCommon()
        winCommon.connectInit(device.id,device.zWinUser,device.zWinPassword)
        return "QMNAME",winCommon.getManagers()

        
