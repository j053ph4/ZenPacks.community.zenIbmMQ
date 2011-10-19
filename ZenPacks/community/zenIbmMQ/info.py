from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos import ProxyProperty
from zope.interface import implements
from ZenPacks.community.zenIbmMQ.interfaces import IMQManagerInfo
from ZenPacks.community.zenIbmMQ.interfaces import IMQQueueInfo
from ZenPacks.community.zenIbmMQ.interfaces import IMQChannelInfo

class MQManagerInfo(ComponentInfo):
    implements(IMQManagerInfo)
    managerName = ProxyProperty("managerName")
    managerStatus = ProxyProperty("managerStatus")

class MQQueueInfo(ComponentInfo):
    implements(IMQQueueInfo)
    queueName = ProxyProperty("queueName")
    queueType = ProxyProperty("queueType")
    queueManager = ProxyProperty("queueManager")
    queueMaxDepth = ProxyProperty("queueMaxDepth")

class MQChannelInfo(ComponentInfo):
    implements(IMQChannelInfo)
    channelName = ProxyProperty("channelName")
    channelConn = ProxyProperty("channelConn")
    channelType = ProxyProperty("channelType")
    channelStatus = ProxyProperty("channelStatus")
    channelManager = ProxyProperty("channelManager")

