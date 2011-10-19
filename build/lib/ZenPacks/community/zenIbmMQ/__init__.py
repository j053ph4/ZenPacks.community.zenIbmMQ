import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused

unused(Globals)

class ZenPack(ZenPackBase):

    packZProperties = [
        ('zMqRunsOnUnix', 'True', 'boolean'),
        ]

    def install(self, dmd):
        ZenPackBase.install(self, dmd)
        pass

    def remove(self, dmd, leaveObjects=False):
        if not leaveObjects:
            pass

        ZenPackBase.remove(self, dmd, leaveObjects=leaveObjects)

