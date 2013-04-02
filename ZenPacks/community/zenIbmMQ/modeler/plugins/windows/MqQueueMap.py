from ZenPacks.community.zenIbmMQ.Common import *
from ZenPacks.community.zenIbmMQ.Definition import *

class MqQueueMap(MQComponentMap,PythonPlugin):
    """
    """
    constr = Construct(DefinitionQueue)
    
    compname = "os"
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    transport = "python"
    
    bundleKey = "QUEUE"

        
