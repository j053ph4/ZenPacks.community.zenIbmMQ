from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

class IMQManagerInfo(IComponentInfo):
    managerName = schema.Text(title=_t(u"Manager Name"))
    managerStatus = schema.Text(title=_t(u"Manager State"))
 
class IMQQueueInfo(IComponentInfo):
    queueName = schema.Text(title=_t(u"Queue Name"))
    queueType = schema.Text(title=_t(u"Queue Type"))
    queueManager = schema.Text(title=_t(u"Queue Manager"))
    queueMaxDepth = schema.Int(title=_t(u"Queue Max Depth"))
    
class IMQChannelInfo(IComponentInfo):
    channelName = schema.Text(title=_t(u"Channel Name"))
    channelConn = schema.Text(title=_t(u"Channel Connection"))
    channelType = schema.Text(title=_t(u"Channel Type"))
    channelStatus = schema.Text(title=_t(u"Channel State"))
    channelManager = schema.Text(title=_t(u"Channel Manager"))
