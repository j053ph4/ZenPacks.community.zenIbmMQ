import os,re
import logging
log = logging.getLogger('zen.zenIbmMQFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from MQManager import *
from .interfaces import *

class zenIbmMQFacade(ZuulFacade):
    implements(IzenIbmMQFacade)
 

    def addMQManager(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenIbmMQ.MQManager import MQManager
        import re
        cid = 'mqmanager' 
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = MQManager(id)
        relation = target.os.mQManagers
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
    
    
    

    	return True, _t("Added MQ Manager for device " + target.id)

    def addMQChannel(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenIbmMQ.MQChannel import MQChannel
        import re
        cid = 'mqchannel' 
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = MQChannel(id)
        relation = target.os.mQChannels
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
    
    
    

    	return True, _t("Added MQ Channel for device " + target.id)

    def addMQQueue(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenIbmMQ.MQQueue import MQQueue
        import re
        cid = 'mqqueue' 
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = MQQueue(id)
        relation = target.os.mQQueues
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
    
    
    

    	return True, _t("Added MQ Queue for device " + target.id)

