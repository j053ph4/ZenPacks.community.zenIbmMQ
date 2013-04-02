from ZenPacks.community.zenIbmMQ.Common import *
from ZenPacks.community.zenIbmMQ.Definition import *

class MqManagerMap(MQComponentMap,CommandPlugin):
    """
    """
    constr = Construct(DefinitionManager)
    
    compname = "os"
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    bundleKey = "QMNAME"
    
    command = 'su - mqm -c dspmq'
    
    

