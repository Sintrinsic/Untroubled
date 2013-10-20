'''
Created on Oct 12, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui
from untroubled.billing.billingAccount import billingAccount


class ChatSession(QtGui.QStandardItem):
    '''
    Container for all the key components of a chat:
    Contains the main dataWidget for the chat, and exposes methods to unify/control/automate its features. 
    Maintains billing page login in case of php-session loss.    
    '''


    def __init__(self, name, dataWidget,  cmdExecutor):
        super(ChatSession,self).__init__(QtCore.QString(name))
        self.dataWidget = dataWidget #main data frame for this specific chat.        
        self.billingBrowser = dataWidget.QWebView_billing
        self.cmdExecutor = cmdExecutor
        self.billingPages = {} #List of billingAccount objects for this chat session [selectedBool,verifiedBool,email, url, object]
        #Message timers to calculate wait times/colors
        self.billingAccounts = {}
        self.lastMsgUser = 0
        self.lastMsgAdmin = 0
        self.loggedInStatus = 0
        self.loginCreds = open("../login").read().split(" ")
        self.billingBrowser.urlChanged.connect(self.billingLogin)
        self.queuedUrl = False
        

    
    def runCommand(self, commandString):
        return self.cmdExecutor.runCommand(commandString)
    
    '''
    Billing tends to drop session when logged in from multiple browsers. The url>login>queue system forces all
    page loads to verify that it's logged in before going to the new billing page. 
    '''
    def setUrl(self, url):
        self.queuedUrl = url
        self.billingLogin()
    
    def runUrlQueue(self):
        if self.queuedUrl:
            self.billingBrowser.setUrl(QtCore.QUrl(QtCore.QString(self.queuedUrl)))
            self.populateBilling()
            self.queuedUrl = False

    
    def billingLogin(self):
        currentUrl = str(self.billingBrowser.url())
        if "login" in currentUrl and self.loggedInStatus > 0:
            self.loggedInStatus = 0
        if self.loggedInStatus < 2:
            if self.loggedInStatus == 1 and "login" not in currentUrl:
                self.loggedInStatus = 2
                self.runUrlQueue()
                return True
            self.billingBrowser.page().mainFrame().evaluateJavaScript("formfield.username.value='"+self.loginCreds[0]+"';formfield.password.value='"+self.loginCreds[1]+"';formfield.submit()")
            self.loggedInStatus = 1 
            QtCore.QTimer.singleShot(3000, self.billingLogin)
            print "Trying login for "+str(self)
            return False
        self.runUrlQueue()
        return True

    def addBilling(self,url):
        if not self.billingPages.has_key(url) and url != self.queuedUrl:
            self.billingPages[url]=url
            self.setUrl(url)
    
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
            


        
    
        