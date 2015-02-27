from ZenPacks.community.zenIbmMQ.Definition import *
from ZenPacks.community.zenIbmMQ.lib.Common import *

__doc__ = """MqQueueMap

MqQueueMap detects IBM MQ Managers.
This version adds a relation to associated mqmanagers.

"""

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
        
