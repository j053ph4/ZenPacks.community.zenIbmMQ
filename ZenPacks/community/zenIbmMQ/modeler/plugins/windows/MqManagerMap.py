from ZenPacks.community.zenIbmMQ.Common import *
from ZenPacks.community.zenIbmMQ.Definition import *

class MqManagerMap(MQComponentMap,PythonPlugin):
    """
    """
    constr = Construct(DefinitionManager)
    
    compname = "os"
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    transport = "python"
    
    bundleKey = "QMNAME"
        
