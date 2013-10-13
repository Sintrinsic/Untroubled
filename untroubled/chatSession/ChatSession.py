'''
Created on Oct 12, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui

class ChatSession(object):
    '''
    Container for all the key components of a chat:
    Contains the main dataWidget for the chat, and exposes methods to unify/control/automate its features. 
    Maintains billing page login in case of php-session loss.    
    '''


    def __init__(self, name, dataWidget, billingBrowser, chatShellManager):
        self.billingBrowser = billingBrowser
        self.dataWidget = dataWidget #main data frame for this specific chat.        
        self.chatShell = chatShellManager.allocateChatShell()
        
        self.nameObject = QtGui.QTreeWidgetItem(QtCore.QString(name))
        self.billingPages = [] #List of billingAccount objects for this chat session [selectedBool,verifiedBool,email, url, object]

        #Message timers to calculate wait times/colors
        self.lastMsgUser = 0
        self.lastMsgAdmin = 0
        
    def addBilling(self,url):
        pass
    
    def removeBilling(self,url):
        pass
    
    def verifyBilling(self,email):
        pass
    
    def runCommand(self, commandString):
        return self.chatShell.runCommand(commandString)
    
    
    
        

        
    
        