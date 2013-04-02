from ZenPacks.community.zenIbmMQ.Common import *
from ZenPacks.community.zenIbmMQ.Definition import *

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

        
