from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class MQChannel(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'MQChannel'
    
    channelManager = 'Stopped'
    channelType = ''
    channelName = ''
    channelConn = 'Stopped'
    channelStatus = 'Stopped'

    _properties = (
    {'id': 'channelManager', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelType', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelConn', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelStatus', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'mQChannels')),
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

class MQChannel(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'MQChannel'
    
    channelManager = 'Stopped'
    channelType = ''
    channelName = ''
    channelConn = 'Stopped'
    channelStatus = 'Stopped'

    _properties = (
    {'id': 'channelManager', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelType', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelConn', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelStatus', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'mQChannels')),
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

class MQChannel(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'MQChannel'
    
    channelManager = 'Stopped'
    channelType = ''
    channelName = ''
    channelConn = 'Stopped'
    channelStatus = 'Stopped'

    _properties = (
    {'id': 'channelManager', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelType', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelName', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelConn', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'channelStatus', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'mQChannels')),
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


