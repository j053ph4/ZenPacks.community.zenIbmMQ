import sys, os, re
import Globals
from optparse import OptionParser
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from Products.ZenUtils.Utils import zenPath,prepId
from twisted.internet.utils import getProcessOutput

class MQHandler(object):
    """ Class dealing with runmqsc data output
    """
    def __init__(self, lines=[]):
        self.data = None
        self.lines = lines
        self.cleanlines = []
        self.info = {}
        self.results = []
    
    def dataMap(self):
        """ parse the lines of input data
        """
        self.info = {}
        if len(self.lines) > 0 and len(self.cleanlines) == 0: self.cleanLines()
        for line in self.cleanlines:
            if '(' not in line or ')'  not in line:  continue
            if 'Copyright' in line: continue
            if 'DISPLAY' in line: continue
            self.info.update(self.getKeyVal(line))
        return self.info
    
    def cleanLines(self):
        """ return a list of cleaned lines """
        self.cleanlines = []
        for line in self.lines:
            line = line.lstrip().rstrip().replace('( )','()')
            line = re.sub("\s\s+",'|',line)
            values = line.split('|')
            if len(values) > 1:
                for v in values: self.cleanlines.append(v)
            else: self.cleanlines.append(line)
        return self.cleanlines
    
    def getKeyVal(self, data):
        idx = data.find("(")
        key = data[0:idx]
        value = data[idx+1:len(data)-1]
        return {key:value}
    
    def parseData(self, key):
        if len(self.lines) > 0 and len(self.cleanlines) == 0: self.cleanLines()
        self.results = []
        keyMap = {'QUEUE' : 'AMQ8409', 'CHANNEL' : 'AMQ8414', 'QMNAME' : 'QMNAME', 'VERSION' : 'VERSION'}
        data = {}
        for line in self.cleanlines:
            # this part is for getting rid of unwanted data
            if key in keyMap.keys():
                if keyMap[key] in line:
                    if key is 'QMNAME':
                        if len(data.keys()) > 0:  self.results.append(data)
                    else:
                        if len(data.keys()) > 1: self.results.append(data)
                    data = {}
                    if key is not 'QMNAME': continue
            if '(' not in line or ')'  not in line:  continue
            if 'Copyright' in line: continue
            data.update(self.getKeyVal(line))
        if key is 'QMNAME':
            if len(data.keys()) > 0:  self.results.append(data)
        else:
            if len(data.keys()) > 1: self.results.append(data)
        return self.results

