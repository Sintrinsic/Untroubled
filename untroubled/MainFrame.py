# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainNoData.ui'
#
# Created: Thu Oct  3 22:16:53 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit
import re, numpy
from untroubled.chatSession import  sessionManager, dataWidget
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtCore.QObject):
    def __init__(self, chatshell,MainWindow):
        super(Ui_MainWindow,self).__init__(MainWindow)
        self.chatshell = chatshell
        self.activeClient = ""  
        self.clientListView = ""  
        self.clients = {}     
       
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1039, 644)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.dashboard = QtWebKit.QWebView(self.frame)
        #self.dashboard.setUrl(QtCore.QUrl(_fromUtf8("http://dashboard.hostgator.com")))
        self.dashboard.setUrl(QtCore.QUrl(_fromUtf8("http://dashboard.hostgator.com")))
        self.dashboard.setObjectName(_fromUtf8("dashboard"))
        self.dashboard.resize(QtCore.QSize(1,1))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #self.horizontalLayout.addWidget(self.dashboard)
        self.frame_clients = QtGui.QFrame(self.frame)
        self.frame_clients.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_clients.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_clients.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_clients.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_clients.setObjectName(_fromUtf8("frame_clients"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_clients)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.frame_clients)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.listView = QtGui.QListView(self.frame_clients)
        self.listView.setViewMode(QtGui.QListView.ListMode)
        self.listView.setFont(QtGui.QFont("Arial",12))
        self.listView.setSpacing(3)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout.addWidget(self.frame_clients)       
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        
        ''' Start Custom '''
        
        self.dashboard.loadFinished.connect(self.dbLogin)
        self.chats = sessionManager.sessionManager(self.frame,self.horizontalLayout,self.listView,self.dashboard)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.startCheck)

        ''' End Custom '''
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        

          
    def getChats(self):
        '''     messages                 : [],
                chatId                   : startingDetails.chatId,
                lastMessageReceived      : 0,
                lastCustomerMessageTime  : 0,
                lastStaffMessageTime     : 0,
                happiness                : 0,
                firstMessageTimestamp    : startingDetails.firstMessageTimestamp || 0,
                chattingAs               : startingDetails.chattingAs || parent.chattingAs,
                showInAssignedChatsList  : startingDetails.showInList===false?false:true,
                isActive                 : true,
                lastNoteRecieved         : 0,
                viewingChatRetroactively : startingDetails.viewingChatRetroactively || false,
                chatRating               : undefined,
                isVerified               : false,
                isVerifiedManually       : false,
                isPinned                 : startingDetails.isPinned || false,
                billingUrl               : false
                DashboardChatWidgets.chats[chat].customerName       
            '''
        print "gotChats"
        self.dbLogin()
        #self.chats[chatId].getChatDetails()        
    
    
    def dbLogin(self,success):
        QtCore.QTimer.singleShot(2000, self.dbLoginTrue)
        print "login fired"
        #self.dashboard.page().mainFrame().addToJavaScriptWindowObject("unt", self)
        #self.dashboard.page().mainFrame().evaluateJavaScript("function check(){unt.chatCallback('hello');setTimeout(function(){check()},2000)}")
        #self.dashboard.page().mainFrame().evaluateJavaScript("check();") 
    
    def dbLoginTrue(self):
        print "logintrue fired"
        self.dashboard.page().mainFrame().evaluateJavaScript("DashboardChatWidgets.staffLogin('bdupree','Bgd938784')")        
        self.dashboard.page().mainFrame().addToJavaScriptWindowObject("unt", self)
        QtCore.QTimer.singleShot(2000, self.startCheck)


    def startCheck(self):    
        print "Updating Chats"    
        self.dashboard.page().mainFrame().evaluateJavaScript('cList = "";for(chat in DashboardChatWidgets.chats){if(DashboardChatWidgets.chats[chat].clientId > 1){DashboardChatWidgets.chats[chat].billingUrl="https://gbadmin.hostgator.com/client/"+DashboardChatWidgets.chats[chat].clientId;cList += DashboardChatWidgets.chats[chat].chatId +","+DashboardChatWidgets.chats[chat].customerName+","+DashboardChatWidgets.chats[chat].billingUrl+","+DashboardChatWidgets.chats[chat].start+"|"}')
        self.dashboard.page().mainFrame().evaluateJavaScript("unt.chatCallback(cList)")
        QtCore.QTimer.singleShot(4000, self.startCheck)


    def fakeCallback(self):
        self.chatCallback("1245323,Brandon,http://google.com,12354|845823,Bob,http://google.com,12354|1123556,tom,http://google.com,12354")
        
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
        self.chats.assessChats(chats)
                
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Untrouble", None))
        self.pushButton.setText(_translate("MainWindow", "New", None))

