from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class MQChannel(DeviceComponent, ManagedEntity):
    """
    MQChannel is an MQ channel
    """
    meta_type = portal_type = "MQChannel"

    channelName = ''
    channelConn = ''
    channelType = ''
    channelStatus = ''
    channelManager = ''
    status = 1

    _properties = ManagedEntity._properties + (
        {'id': 'channelName', 'type': 'string', 'mode': ''},
        {'id': 'channelConn', 'type': 'string', 'mode': ''},
        {'id': 'channelType', 'type': 'string', 'mode': ''},
        {'id': 'channelStatus', 'type': 'string', 'mode': ''},
        {'id': 'channelManager', 'type': 'string', 'mode': ''},
        {'id': 'status', 'type':'int', 'mode':''},
    )

    _relations = ManagedEntity._relations + (
        ('mqDevice', ToOne(ToManyCont,
            'ZenPacks.community.zenIbmMQ.MQDevice.MQDevice',
            'mqChannel',
            ),
        ),
        ('mqManager', ToOne(ToManyCont,
            'ZenPacks.community.zenIbmMQ.MQManager.MQManager',
            'mqChannel',
            ),
        ), 
    )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)
    
    def viewName(self):
        """ 
        """
        return self.channelName
    
    titleOrId = name = viewName
    
    def primarySortKey(self):
        """ 
        """
        return self.channelName
            
    def device(self):
        """ 
        """
        return self.mqDevice()
    
    def monitored(self):
        """ 
        """
        return True
    
    def getStatus(self):
        """ 
        """
        return self.statusMap()

    def statusMap(self):
        """ map run state to zenoss status
        """
        if self.channelStatus == 'RUNNING':
            self.status = 0
        elif self.channelStatus == 'STOPPED':
            self.status = 2
        else:
            self.status = -1
        return self.status

    
