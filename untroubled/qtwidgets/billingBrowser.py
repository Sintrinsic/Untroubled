'''
Created on Oct 30, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui, QtWebKit


class BillingBrowser(QtWebKit.QWebView):

    def __init__(self, chatSession, parent=None):
        super(BillingBrowser,self).__init__(parent)
        self.chatSession = chatSession
        self.loggedInStatus = 0
        self.loginCreds = open("../login").read().split(" ")
        self.setUrl(QtCore.QUrl(QtCore.QString("https://gbadmin.hostgator.com")))
        self.loadFinished.connect(self.billingLogin)
        self.queuedUrl = False
        self.chatSession.eventHandler.register("navEvent", self.navResponse)
        self.setStyleSheet(QtCore.QString("background-color:none;"))
        
    '''
    Billing tends to drop session when logged in from multiple browsers. The url>login>queue system forces all
    page loads to verify that it's logged in before going to the new billing page. 
    '''
    def queueSetUrl(self, url):
        self.queuedUrl = url
        self.billingLogin()
    
    def runUrlQueue(self):
        if self.queuedUrl:
            self.setUrl(QtCore.QUrl(QtCore.QString(self.queuedUrl)))
            self.queuedUrl = False
    
    def billingLogin(self):
        currentUrl = str(self.url())
        if "login" in currentUrl and self.loggedInStatus > 0:
            self.loggedInStatus = 0
        if self.loggedInStatus < 2:
            if self.loggedInStatus == 1 and "login" not in currentUrl:
                self.loggedInStatus = 2
                self.runUrlQueue()
                return True
            self.page().mainFrame().evaluateJavaScript("formfield.username.value='"+self.loginCreds[0]+"';formfield.password.value='"+self.loginCreds[1]+"';formfield.submit()")
            self.loggedInStatus = 1 
            QtCore.QTimer.singleShot(3000, self.billingLogin)
            print "Trying login for "+str(self)
            return False
        self.runUrlQueue()
        return True
    
    def navResponse(self, event):
        if self.chatSession.dataWidget.selected:
            if event.navOption == "Gatorbill":
                self.setVisible(True)
            else: 
                self.setVisible(False)
    