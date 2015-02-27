from ZenPacks.community.zenIbmMQ.Definition import *
from ZenPacks.community.zenIbmMQ.lib.Common import *

__doc__ = """MqQueueMap

MqQueueMap detects IBM MQ Queues.
This version adds a relation to associated mqmanagers.

"""

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

        
