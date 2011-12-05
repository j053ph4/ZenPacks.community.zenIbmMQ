from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class MQManager(DeviceComponent, ManagedEntity):
    """
    MQManager is an MQ manager
    """
    meta_type = portal_type = "MQManager"

    managerName = ''
    managerStatus = 'Stopped'
    status = 1

    _properties = ManagedEntity._properties + (
        {'id': 'managerName', 'type': 'string', 'mode': ''},
        {'id': 'managerStatus', 'type': 'string', 'mode': ''},
        {'id': 'status', 'type':'int', 'mode':''},
    )

    _relations = ManagedEntity._relations + (
        ('mqDevice', ToOne(ToManyCont,
            'ZenPacks.community.zenIbmMQ.MQDevice.MQDevice',
            'mqManager',
            ),
        ),
        ('mqQueues', ToManyCont(ToOne,
            'ZenPacks.community.zenIbmMQ.MQQueue.MQQueue',
            'mqManager',
            ),
        ), 
        ('mqChannels', ToManyCont(ToOne,
            'ZenPacks.community.zenIbmMQ.MQChannels.MQChannels',
            'mqManager',
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
        return self.managerName
    
    titleOrId = name = viewName
    
    def primarySortKey(self):
        """ 
        """
        return self.managerName
            
    def getStatus(self):
        """ 
        """
        return self.statusMap()

    def device(self):
        """ 
        """
        return self.mqDevice()

    def statusMap(self):
        """ map run state to zenoss status
        """
        runValue = self.getStatusValue()
        if runValue == 1:
            self.managerStatus == 'Running'
            self.status = 0
        else:
            self.managerStatus == 'Stopped'
            self.status = 2
        return self.status
    
    def getStatusValue(self):
        """ return numerical value of status check [1|0]
        """
        d = self.device()
        if d.zMqRunsOnUnix == True:
            datapoint = 'mgr-status-nix_status'
        else:
            datapoint = 'mgr-status-win_status'
        return int(self.cacheRRDValue(datapoint,0))
    
    def manage_deleteComponent(self, REQUEST=None):
        url = None
        if REQUEST is not None:
            url = self.device().mqManagers.absolute_url()
        self.getPrimaryParent()._delObject(self.id)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)
