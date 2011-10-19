from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class MQQueue(DeviceComponent, ManagedEntity):
    """
    MQComponent is an MQ queue
    """
    meta_type = portal_type = "MQQueue"

    queueName = ''
    queueType = ''
    queueManager = ''
    queueMaxDepth = 1
    status = 0

    _properties = ManagedEntity._properties + (
        {'id': 'queueName', 'type': 'string', 'mode': ''},
        {'id': 'queueType', 'type': 'string', 'mode': ''},
        {'id': 'queueManager', 'type': 'string', 'mode': ''},
        {'id': 'queueMaxDepth', 'type': 'int', 'mode': ''},
        {'id': 'status', 'type':'int', 'mode':''},
    )

    _relations = ManagedEntity._relations + (
        ('mqDevice', ToOne(ToManyCont,
            'ZenPacks.community.zenIbmMQ.MQDevice.MQDevice',
            'mqQueue',
            ),
        ),
        ('mqManager', ToOne(ToManyCont,
            'ZenPacks.community.zenIbmMQ.MQManager.MQManager',
            'mqQueue',
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
        return self.queueName
    
    titleOrId = name = viewName
    
    def primarySortKey(self):
        """ 
        """
        return self.queueName
            
    def getStatus(self):
        """ 
        """
        self.status = 0
        return self.status

    def getMaxDepth(self):
        """
        """
        return float(self.queueMaxDepth)
    
    def device(self):
        """ 
        """
        return self.mqDevice()
    
    def monitored(self):
        """ 
        """
        return True


    
