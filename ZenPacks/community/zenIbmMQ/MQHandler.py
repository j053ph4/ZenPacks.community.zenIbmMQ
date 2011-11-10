import sys, os, re
import Globals
from optparse import OptionParser
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from Products.ZenUtils.Utils import zenPath,prepId
from twisted.internet.utils import getProcessOutput

class MQParser():
    """ Class dealing with runmqsc data output
    """
    def __init__(self):
        self.data = None
        self.lines = []
        self.info = {}

    def dataMap(self):
        """ parse the lines of input data
        """
        self.lines = self.cleanLines()
        for line in self.lines:
            key,value = self.keyValue(line)
            self.info[key] = value
            
    def cleanLines(self):
        """ return a list of cleaned lines
        """
        newlines = []
        for line in self.lines:
            line = line.replace('\r','')
            if re.search("\(",line) != None and re.search("\)",line) != None:
                line = line.replace('( )','()')
                line = line.split('  ')
                for item in line:
                    item = item.strip()
                    if len(item) > 1:
                        newlines.append(item)
        return newlines

    def fixReturns(self):
        """ convert Windows newline format to unix
        """
        newlines = []
        for line in self.lines:
            line = line.replace('\r','')
            newlines.append(line)
        return newlines
    
    def keyValue(self,data):
        """ pull the data from MQ's data format, e.g.
                ATTRIB(VALUE)
        """
        attrib = data[0:data.find("(")]
        value = data[data.find("(")+1:len(data)-1]
        if value == None:
            value = ''
        return attrib,value
    
    def bundleData(self,lines,beginString,midString,endString):
        """ bundle up the resulting data into lists of lists
        """
        output = []
        bundle = []
        reset = False
        for line in lines:
            if re.search(beginString,line) != None: # new manager
                reset = True
            elif re.search(midString,line) != None: # new queue
                reset = True
            elif re.search(endString,line) != None: # last line
                reset = True
            else:
                bundle.append(line)
            if reset == True:
                output.append(bundle)
                bundle = []
                reset = False
        return output
        
