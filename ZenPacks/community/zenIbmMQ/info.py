from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenIbmMQ.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class MQManagerInfo(ComponentInfo):
    implements( IMQManagerInfo )
    managerStatus = ProxyProperty('managerStatus')
    managerName = ProxyProperty('managerName')


from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenIbmMQ.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class MQChannelInfo(ComponentInfo):
    implements( IMQChannelInfo )
    channelManager = ProxyProperty('channelManager')
    channelType = ProxyProperty('channelType')
    channelName = ProxyProperty('channelName')
    channelConn = ProxyProperty('channelConn')
    channelStatus = ProxyProperty('channelStatus')


from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenIbmMQ.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class MQQueueInfo(ComponentInfo):
    implements( IMQQueueInfo )
    queueType = ProxyProperty('queueType')
    queueName = ProxyProperty('queueName')
    queueManager = ProxyProperty('queueManager')
    queueMaxDepth = ProxyProperty('queueMaxDepth')


