'''
Created on Oct 12, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui
from untroubled.billing.billingAccount import billingAccount
from untroubled.qtwidgets.sessionLabel import sessionLabel
from untroubled.qtwidgets.billingBrowser import BillingBrowser
from untroubled.qtwidgets.dataWidget import dataWidget
from untroubled.event.ChatEvent import ChatEvent

class ChatSession(object):
    '''
    Container for all the key components of a chat:
    Contains the main dataWidget for the chat, and exposes methods to unify/control/automate its features. 
    Maintains billing page login in case of php-session loss.    
    '''


    def __init__(self, name, ID, cmdExecutor, eventManager):
        self.name = name
        self.ID = ID  
        self.cmdExecutor = cmdExecutor
        self.eventHandler = eventManager
        self.label = sessionLabel(self.name, None, self)
        self.dataWidget = dataWidget(None, eventManager, ID)
        self.billingBrowser = BillingBrowser(self.dataWidget)
        self.billingPages = {} #List of billingAccount objects for this chat session [selectedBool,verifiedBool,email, url, object]
        #Message timers to calculate wait times/colors
        self.billingAccounts = {}
        self.lastMsgUser = 0
        self.lastMsgAdmin = 0

    def addBilling(self,url):
        if not self.billingPages.has_key(url) and url != self.queuedUrl:
            self.billingPages[url]=url
            self.billingBrowser.setUrl(url)
    
    def removeBilling(self,url):
        pass
    
    def verifyBilling(self,email):
        pass
    
    def checkForBilling(self,url):
        if str(url) in self.billingPages:
            return True
        return False    
        
    def populateBilling(self):
        if self.queuedUrl and not self.billingAccounts.has_key(self.queuedUrl):
            self.billingAccounts[self.queuedUrl] = billingAccount(self.queuedUrl,self.billingBrowser.page().mainFrame())
            
    def select(self):
        closedEvent = ChatEvent("manual_selectChat", self.ID, "select", self)
        self.eventHandler.call("chatEvent",closedEvent)
        
    def remove(self):
        closedEvent = ChatEvent("manual_removeChat", self.ID, "remove", self)
        self.eventHandler.call("chatEvent",closedEvent)


        
    
        