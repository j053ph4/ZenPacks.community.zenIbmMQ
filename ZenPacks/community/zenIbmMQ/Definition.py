from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

ROOT = "ZenPacks.community"
BASE = "zenIbmMQ"
VERSION = Version(2, 5, 0)
ZPROPS = [
          ('zMqRunsOnUnix', True, 'boolean'),
          ('zMqUsername', 'mqm', 'boolean')
          ]

managerRunStateMap = {
               4: 'Running',
               3: 'Online',
               2: 'Unavailable',
               1: 'Stopped',
               0: 'Shutdown',
               -1: 'Unknown',
               }

def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'Unknown'
    
def getManagerRunState(ob): return ob.getMapValue('status_status', ob.managerRunStateMap)


DefinitionManager = type('DefinitionManager', (BasicDefinition,),{
        'version' : VERSION,
        'zenpackbase': BASE,
        'packZProperties' : ZPROPS,
        'component' : 'MQManager',
        'componentData' : {
                          'singular': 'MQ Manager',
                          'plural': 'MQ Managers',
                          'displayed': 'managerName', # component field in Event Console
                          'primaryKey': 'managerName',
                          'properties': {
                                         'managerName' : addProperty('Name','Basic','',optional=False),
                                         'managerStatus' : addProperty('State','Basic',''),
                                         'getManagerRunState' : getReferredMethod('Current State', 'getManagerRunState'),
                                         'eventClass' : addProperty('Event Class','Display Settings','/App/MQ'),
                                         },
                          },
        'componentAttributes' : { 'managerRunStateMap': managerRunStateMap, },
        'componentMethods' : [getMapValue, getManagerRunState ],                                       
        }
)


addDefinitionSelfComponentRelation(DefinitionManager,
                          'mqmanager', ToOne, '%s.%s.%s' % (ROOT, BASE, 'MQManager'),'managerName',
                          'osprocess',  ToOne, 'Products.ZenModel.OSProcess', 'displayName',
                          'OS Process', 'displayName')


DefinitionChannel = type('DefinitionChannel', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MQChannel',
        'componentData' : {
                          'singular': 'MQ Channel',
                          'plural': 'MQ Channels',
                          'displayed': 'id', # component field in Event Console
                          'primaryKey': 'id',
                          'properties': {
                                         'channelName' : addProperty('Name',optional=False),
                                         'channelConn' : addProperty('Connection','Basic','Stopped',optional=False),
                                         'channelType' : addProperty('Type','Basic','',optional=False),
                                         'channelStatus' : addProperty('State','Basic','Stopped',optional=False),
                                         'channelManager' : addProperty('Manager','Basic','Stopped',optional=False),
                                         'eventClass' : addProperty('Event Class','Display Settings','/App/MQ'),
                                         },
                          },
        'componentMethods': [],
        }
)

addDefinitionSelfComponentRelation(DefinitionChannel,
                          'mqchannels', ToMany, 'ZenPacks.community.zenIbmMQ.MQChannel','channelManager',
                          'mqmanager',  ToOne, 'ZenPacks.community.zenIbmMQ.MQManager', 'managerName',
                          "MQ Manager")


DefinitionQueue = type('DefinitionQueue', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'MQQueue',
        'componentData' : {
                  'singular': 'MQ Queue',
                  'plural': 'MQ Queues',
                  'displayed': 'queueName', # component field in Event Console
                  'primaryKey': 'queueName',
                  'properties': {
                                 'queueName' : addProperty('Name','Basic','',optional=False),
                                 'queueType' : addProperty('Type','Basic','',optional=False),
                                 'queueManager' : addProperty('Manager','Basic','',optional=False),
                                 'queueMaxDepth' : addProperty('Max Depth','Basic','',optional=False),
                                 'eventClass' : addProperty('Event Class','Display Settings','/App/MQ'),
                                 },
                  },
        'componentMethods': [],
        }
)

addDefinitionSelfComponentRelation(DefinitionQueue,
                          'mqqueues', ToMany, 'ZenPacks.community.zenIbmMQ.MQQueue','queueManager',
                          'mqmanager',  ToOne, 'ZenPacks.community.zenIbmMQ.MQManager', 'managerName',
                          "MQ Manager")

