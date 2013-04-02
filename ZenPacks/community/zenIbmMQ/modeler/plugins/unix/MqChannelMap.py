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

    bundleKey = "CHANNEL"
    
    command = '''for LINE in $(dspmq|awk '{print $1}'); \
do MGR=$(echo $LINE | cut -f 2 -d '(' | cut -f 1 -d ')');\
printf \"QueueManager ${MGR}\n\";\
echo 'DISPLAY CHSTATUS(*) ALL' | su - mqm -c \"runmqsc $MGR\" ; done'''

