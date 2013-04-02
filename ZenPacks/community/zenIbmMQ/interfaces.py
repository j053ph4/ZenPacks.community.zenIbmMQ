from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IMQManagerInfo(IComponentInfo):
    ''''''
    managerStatus = SingleLineText(title=_t(u'State'))
    managerName = SingleLineText(title=_t(u'Name'))



class IMQChannelInfo(IComponentInfo):
    ''''''
    channelManager = SingleLineText(title=_t(u'Manager'))
    channelType = SingleLineText(title=_t(u'Type'))
    channelName = SingleLineText(title=_t(u'Name'))
    channelConn = SingleLineText(title=_t(u'Connection'))
    channelStatus = SingleLineText(title=_t(u'State'))



class IMQQueueInfo(IComponentInfo):
    ''''''
    queueType = SingleLineText(title=_t(u'Type'))
    queueName = SingleLineText(title=_t(u'Name'))
    queueManager = SingleLineText(title=_t(u'Manager'))
    queueMaxDepth = SingleLineText(title=_t(u'Max Depth'))



class IzenIbmMQFacade(IFacade):
    ''''''

    def addMQManager(self, ob, **kwargs):
        ''''''

    def addMQChannel(self, ob, **kwargs):
        ''''''

    def addMQQueue(self, ob, **kwargs):
        ''''''


