'''
Created on Oct 12, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui

class ChatSession(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        self.nameObject = QtGui.QTreeWidgetItem(QtCore.QString(name))
        self.billingUrl = ""
        self.dataWidget = None
        self.packageSchema = []
        self.invoices = []
        