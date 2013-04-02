from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class MQQueue(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'MQQueue'
    
    queueType = ''
    queueName = ''
    queueManager = ''
    queueMaxDepth = ''

    _properties = (
    {'id': 'queueType', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueManager', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueMaxDepth', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'mQQueues')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class MQQueue(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'MQQueue'
    
    queueType = ''
    queueName = ''
    queueManager = ''
    queueMaxDepth = ''

    _properties = (
    {'id': 'queueType', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueManager', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueMaxDepth', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'mQQueues')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class MQQueue(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'MQQueue'
    
    queueType = ''
    queueName = ''
    queueManager = ''
    queueMaxDepth = ''

    _properties = (
    {'id': 'queueType', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueManager', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'queueMaxDepth', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'mQQueues')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.id
    
    def viewName(self):
        return self.id
    
    name = titleOrId = viewName


