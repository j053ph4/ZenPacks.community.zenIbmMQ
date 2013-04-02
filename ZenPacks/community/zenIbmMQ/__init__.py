import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenModel.Device import Device
from Definition import *
from ZenPacks.community.ConstructionKit.Construct import *
#import os,re,new
unused(Globals)

c = Construct(DefinitionManager)
c.configZCMLEnded = False
d = Construct(DefinitionChannel)
d.configZCMLEnded = False
e = Construct(DefinitionQueue)
e.configZCMLEnded = True

""" Add device relations
"""
OperatingSystem._relations += c.deviceToComponent
OperatingSystem._relations += d.deviceToComponent
OperatingSystem._relations += e.deviceToComponent
setattr(Device, c.addMethodName, stringToMethod(c.addMethodName, c.addMethod))
setattr(Device, d.addMethodName, stringToMethod(d.addMethodName, d.addMethod))
setattr(Device, e.addMethodName, stringToMethod(e.addMethodName, e.addMethod))

# copied from HttpMonitor
def onCollectorInstalled(ob, event):
    zpFriendly = Definition.componentClass
    errormsg = '{0} binary cannot be found on {1}. This is part of the nagios-plugins ' + \
               'dependency, and must be installed before {2} can function.'
    verifyBin = Definition.cmdFile
    code, output = ob.executeCommand('zenbincheck %s' % verifyBin, 'zenoss', needsZenHome=True)
    if code:
        log.warn(errormsg.format(verifyBin, ob.hostname, zpFriendly))

class ZenPack(ZenPackBase):
    """ Zenpack install
    """
    
    packZProperties = c.d.packZProperties
    
    def updateRelations(self):
        for dev in self.dmd.Devices.getSubDevices():
            dev.os.buildRelations()  
    
    def install(self, app):
        c.buildZenPackFiles()
        d.buildZenPackFiles(new=False)
        e.buildZenPackFiles(new=False)
        ZenPackBase.install(self, app)
        self.updateRelations()

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in (c.relname)])
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in (d.relname)])
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in (e.relname)])
        self.updateRelations()
