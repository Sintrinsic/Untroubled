'''
Created on Oct 30, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui

class DashboardInterface(QtCore.QObject):

    def __init__(self, dashboardWebview, sessionManager):
        super(DashboardInterface,self).__init__()
        self.sessionManager = sessionManager
        self.db = dashboardWebview
        self.db.setUrl(QtCore.QUrl(QtCore.QString("http://dashboard.hostgator.com")))
        self.db.loadFinished.connect(self.urlChanged)
        self.login =  open("../login").read().split(" ")
        self.loggedIn = False
                               
    def urlChanged(self):
        print "Dashboard url changed."
        self.testLogin()

        
    def injectLogon(self):
        self.db.page().mainFrame().evaluateJavaScript("DashboardChatWidgets.staffLogin('"+self.login[0]+"','"+self.login[1]+"')")        
    
    def testLogin(self):
        self.db.page().mainFrame().addToJavaScriptWindowObject("dbController", self)
        self.db.page().mainFrame().evaluateJavaScript("dbController.testLoginResp(DashboardChatWidgets.staffId)")        
    
    @QtCore.pyqtSlot(str)   
    def testLoginResp(self, string):
        print "Dashboard Login tested and: "+string
        if string != "false" and not "undefined" in string:
            print "logged into dashboard"
            self.loggedIn = True
            self.startCheck() # Starts the 4 second chat assessment loop. 
        else:
            if not self.loggedIn:
                print "NOT logged into dashboard"
                self.injectLogon()
                self.loggedIn = False
                QtCore.QTimer.singleShot(1000, self.testLogin)
            
    def startCheck(self):    
        print "Updating Chats"    
        self.db.page().mainFrame().evaluateJavaScript('cList = "";for(chat in DashboardChatWidgets.chats){if(DashboardChatWidgets.chats[chat].clientId > 1){DashboardChatWidgets.chats[chat].billingUrl="https://gbadmin.hostgator.com/client/"+DashboardChatWidgets.chats[chat].clientId};cList += DashboardChatWidgets.chats[chat].chatId +","+DashboardChatWidgets.chats[chat].customerName+","+DashboardChatWidgets.chats[chat].billingUrl+","+DashboardChatWidgets.chats[chat].start+"|"}')
        self.db.page().mainFrame().evaluateJavaScript("dbController.chatCallback(cList)")
        QtCore.QTimer.singleShot(4000, self.startCheck)


    @QtCore.pyqtSlot(str)        
    def chatCallback(self,chatList):
        chatList = str(chatList)
        cmds = chatList.split("|")
        chats = []
        for c in cmds:
            if c:
                eles = c.split(",")
                chats.append(eles)
        print "Calling assessChats on "+str(chats)
        self.sessionManager.assessChats(chats)

    