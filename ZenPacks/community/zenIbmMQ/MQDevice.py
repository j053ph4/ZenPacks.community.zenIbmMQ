from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class MQDevice(Device):
    """
    """

    meta_type = portal_type = 'MQDevice'
    
    _relations = Device._relations + (
        ('mqManagers', ToManyCont(ToOne,
            'ZenPacks.community.zenIbmMQ.MQManager.MQManager',
            'mqDevice',
            ),
        ),
        ('mqQueues', ToManyCont(ToOne,
            'ZenPacks.community.zenIbmMQ.MQQueue.MQQueue',
            'mqDevice',
            ),
        ), 
        ('mqChannels', ToManyCont(ToOne,
            'ZenPacks.community.zenIbmMQ.MQChannel.MQChannel',
            'mqDevice',
            ),
        ), 
    )


