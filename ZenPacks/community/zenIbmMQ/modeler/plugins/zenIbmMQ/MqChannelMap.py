from ZenPacks.community.zenIbmMQ.Definition import *
from ZenPacks.community.zenIbmMQ.lib.Common import *

__doc__ = """MqChannelMap

MqChannelMap detects IBM MQ Channels.
This version adds a relation to associated mqmanagers.

"""

class MqChannelMap(MQComponentMap):
    """
    """
    constr = Construct(DefinitionChannel)
    
    compname = "os"
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    transport = "python"
    
    bundleKey = "CHANNEL"

        
