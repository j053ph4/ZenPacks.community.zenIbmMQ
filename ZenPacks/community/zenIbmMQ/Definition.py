from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

ROOT = "ZenPacks.community"
BASE = "zenIbmMQ"
VERSION = Version(2, 0, 0)
ZPROPS = [('zMqRunsOnUnix', True, 'boolean'),
          ('zMqUsername', 'mqm', 'boolean')
          ]
CWD = os.path.dirname(os.path.realpath(__file__))

class DefinitionManager():
    """
    """
    version = VERSION
    zenpackroot = ROOT # ZenPack Root
    zenpackbase = BASE # ZenaPack Name
    #dictionary of components
    component = 'MQManager'
    componentData = {
                  'singular': 'MQ Manager',
                  'plural': 'MQ Managers',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': {
                                 'managerName' : addProperty('Name','Basic','',optional='false'),
                                 'managerStatus' : addProperty('State','Basic','',optional='false'),
                                 },
                  }
    
    packZProperties = ZPROPS
    addManual = False
    #dictionary of datasources
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = CWD # ZenPack files directory
    
class DefinitionChannel():
    """
    """
    version = VERSION
    zenpackroot = ROOT # ZenPack Root
    zenpackbase = BASE # ZenaPack Name
    #dictionary of components
    component = 'MQChannel'
    componentData = {
                  'singular': 'MQ Channel',
                  'plural': 'MQ Channels',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': {
                                 'channelName' : addProperty('Name','Basic','',optional='false'),
                                 'channelConn' : addProperty('Connection','Basic','Stopped',optional='false'),
                                 'channelType' : addProperty('Type','Basic','',optional='false'),
                                 'channelStatus' : addProperty('State','Basic','Stopped',optional='false'),
                                 'channelManager' : addProperty('Manager','Basic','Stopped',optional='false'),
                                 },
                  }
    
    packZProperties = ZPROPS
    addManual = False
    #dictionary of datasources
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = CWD # ZenPack files directory

class DefinitionQueue():
    """
    """
    version = VERSION
    zenpackroot = ROOT # ZenPack Root
    zenpackbase = BASE # ZenaPack Name
    #dictionary of components
    component = 'MQQueue'
    componentData = {
                  'singular': 'MQ Queue',
                  'plural': 'MQ Queues',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': {
                                 'queueName' : addProperty('Name','Basic','',optional='false'),
                                 'queueType' : addProperty('Type','Basic','',optional='false'),
                                 'queueManager' : addProperty('Manager','Basic','',optional='false'),
                                 'queueMaxDepth' : addProperty('Max Depth','Basic','',optional='false'),
                                 },
                  }
    
    packZProperties = ZPROPS
    addManual = False
    #dictionary of datasources
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = CWD # ZenPack files directory
