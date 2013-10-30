# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untroubled2.ui'
#
# Created: Wed Oct 23 20:21:50 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui,  QtWebKit
from untroubled.chatSession.sessionManager import sessionManager
from untroubled.event.EventManager import EventManager

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

class untroubledGui(QtGui.QWidget):
    def __init__(self, parent=None):
        super(untroubledGui, self).__init__(parent)
        self.setupUi(self)
    
    def setupUi(self, untroubled):
        untroubled.setObjectName(_fromUtf8("untroubled"))
        untroubled.resize(929, 497)
        untroubled.setStyleSheet(_fromUtf8("background-color:rgb(80, 80, 80)"))
        self.layout_main = QtGui.QVBoxLayout(untroubled)
        self.layout_main.setSpacing(0)
        self.layout_main.setMargin(0)
        self.layout_main.setObjectName(_fromUtf8("layout_main"))
        self.content_frame = QtGui.QFrame(untroubled)
        self.content_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.content_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.content_frame.setObjectName(_fromUtf8("content_frame"))
        self.layout_content = QtGui.QHBoxLayout(self.content_frame)
        self.layout_content.setSpacing(0)
        self.layout_content.setMargin(0)
        self.layout_content.setObjectName(_fromUtf8("layout_content"))
        self.sessions_main_frame = QtGui.QFrame(self.content_frame)
        self.sessions_main_frame.setMinimumSize(QtCore.QSize(175, 0))
        self.sessions_main_frame.setMaximumSize(QtCore.QSize(175, 16777215))
        self.sessions_main_frame.setStyleSheet(_fromUtf8("background-color:rgb(130, 130, 130);\n"
""))
        self.sessions_main_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.sessions_main_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.sessions_main_frame.setObjectName(_fromUtf8("sessions_main_frame"))
        self.layout_sessions_main = QtGui.QVBoxLayout(self.sessions_main_frame)
        self.layout_sessions_main.setSpacing(0)
        self.layout_sessions_main.setMargin(0)
        self.layout_sessions_main.setObjectName(_fromUtf8("layout_sessions_main"))
        self.sessions_logo_frame = QtGui.QFrame(self.sessions_main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sessions_logo_frame.sizePolicy().hasHeightForWidth())
        self.sessions_logo_frame.setSizePolicy(sizePolicy)
        self.sessions_logo_frame.setMinimumSize(QtCore.QSize(0, 60))
        self.sessions_logo_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.sessions_logo_frame.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.938547 rgba(48, 48, 48, 255), stop:1 rgba(30, 30, 30, 255));\n"
"color:white;\n"
"font-family:arial;\n"
"font-weight:bold;"))
        self.sessions_logo_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.sessions_logo_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.sessions_logo_frame.setObjectName(_fromUtf8("sessions_logo_frame"))
        self.logo_label = QtGui.QLabel(self.sessions_logo_frame)
        self.logo_label.setGeometry(QtCore.QRect(4, 4, 141, 51))
        self.logo_label.setMinimumSize(QtCore.QSize(0, 35))
        self.logo_label.setMaximumSize(QtCore.QSize(175, 9999999))
        self.logo_label.setStyleSheet(_fromUtf8("background-color:none;font-size:14pt;"))
        self.logo_label.setText(_fromUtf8(""))
        self.logo_label.setTextFormat(QtCore.Qt.RichText)
        self.logo_label.setPixmap(QtGui.QPixmap(_fromUtf8("../resources/unt-logo-3dslt.png")))
        self.logo_label.setScaledContents(False)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setMargin(0)
        self.logo_label.setObjectName(_fromUtf8("logo_label"))
        self.layout_sessions_main.addWidget(self.sessions_logo_frame)
        self.sessions_add_button = QtGui.QPushButton(self.sessions_main_frame)
        self.sessions_add_button.setMinimumSize(QtCore.QSize(0, 30))
        self.sessions_add_button.setStyleSheet(_fromUtf8("background-color:rgb(150, 150, 150)"))
        self.sessions_add_button.setFlat(False)
        self.sessions_add_button.setObjectName(_fromUtf8("sessions_add_button"))
        self.layout_sessions_main.addWidget(self.sessions_add_button)
        self.sessions_hline = QtGui.QFrame(self.sessions_main_frame)
        self.sessions_hline.setMinimumSize(QtCore.QSize(20, 10))
        self.sessions_hline.setFrameShape(QtGui.QFrame.HLine)
        self.sessions_hline.setFrameShadow(QtGui.QFrame.Sunken)
        self.sessions_hline.setObjectName(_fromUtf8("sessions_hline"))
        self.layout_sessions_main.addWidget(self.sessions_hline)
        self.sessions_list_frame = QtGui.QFrame(self.sessions_main_frame)
        self.sessions_list_frame.setStyleSheet(_fromUtf8("background-color:rgb(130, 130, 130);\n"
"color:black;"))
        self.sessions_list_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.sessions_list_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.sessions_list_frame.setObjectName(_fromUtf8("sessions_list_frame"))
        self.layout_sessions_list = QtGui.QVBoxLayout(self.sessions_list_frame)
        self.layout_sessions_list.setSpacing(0)
        self.layout_sessions_list.setMargin(0)
        self.layout_sessions_list.setObjectName(_fromUtf8("layout_sessions_list"))
        self.sessions_container_frame = QtGui.QFrame(self.sessions_list_frame)
        self.sessions_container_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.sessions_container_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.sessions_container_frame.setObjectName(_fromUtf8("sessions_container_frame"))
        self.layout_sessions_container = QtGui.QVBoxLayout(self.sessions_container_frame)
        self.layout_sessions_container.setObjectName(_fromUtf8("layout_sessions_container"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_sessions_container.addItem(spacerItem)
        self.layout_sessions_list.addWidget(self.sessions_container_frame)
        self.layout_sessions_main.addWidget(self.sessions_list_frame)
        self.layout_content.addWidget(self.sessions_main_frame)
        self.dataframe_frame_main = QtGui.QFrame(self.content_frame)
        self.dataframe_frame_main.setFrameShape(QtGui.QFrame.NoFrame)
        self.dataframe_frame_main.setFrameShadow(QtGui.QFrame.Plain)
        self.dataframe_frame_main.setObjectName(_fromUtf8("dataframe_frame_main"))
        self.layout_dataframe_main = QtGui.QVBoxLayout(self.dataframe_frame_main)
        self.layout_dataframe_main.setSpacing(0)
        self.layout_dataframe_main.setMargin(0)
        self.layout_dataframe_main.setObjectName(_fromUtf8("layout_dataframe_main"))
        self.dataframe_nav__frame = QtGui.QFrame(self.dataframe_frame_main)
        self.dataframe_nav__frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.dataframe_nav__frame.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(40, 40, 40, 255), stop:0.938547 rgba(48, 48, 48, 255), stop:1 rgba(30, 30, 30, 255));\n"
"color:white;\n"
"font-family:arial;\n"
"font-weight:bold;"))
        self.dataframe_nav__frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dataframe_nav__frame.setFrameShadow(QtGui.QFrame.Plain)
        self.dataframe_nav__frame.setObjectName(_fromUtf8("dataframe_nav__frame"))
        self.layout_dataframe_nav_left = QtGui.QHBoxLayout(self.dataframe_nav__frame)
        self.layout_dataframe_nav_left.setObjectName(_fromUtf8("layout_dataframe_nav_left"))
        self.label = QtGui.QLabel(self.dataframe_nav__frame)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setStyleSheet(_fromUtf8("background-color:none;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.layout_dataframe_nav_left.addWidget(self.label)
        self.line = QtGui.QFrame(self.dataframe_nav__frame)
        self.line.setMinimumSize(QtCore.QSize(30, 0))
        self.line.setStyleSheet(_fromUtf8("background-color:none;"))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layout_dataframe_nav_left.addWidget(self.line)
        self.dataFrame_nav_untroubled_toolbutton = QtGui.QToolButton(self.dataframe_nav__frame)
        self.dataFrame_nav_untroubled_toolbutton.setMinimumSize(QtCore.QSize(0, 30))
        self.dataFrame_nav_untroubled_toolbutton.setStyleSheet(_fromUtf8("background-color:rgba(48, 48, 48, 255)"))
        self.dataFrame_nav_untroubled_toolbutton.setText(_fromUtf8("Untroubled"))
        self.dataFrame_nav_untroubled_toolbutton.setCheckable(False)
        self.dataFrame_nav_untroubled_toolbutton.setAutoRepeat(False)
        self.dataFrame_nav_untroubled_toolbutton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.dataFrame_nav_untroubled_toolbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.dataFrame_nav_untroubled_toolbutton.setAutoRaise(True)
        self.dataFrame_nav_untroubled_toolbutton.setArrowType(QtCore.Qt.NoArrow)
        self.dataFrame_nav_untroubled_toolbutton.setObjectName(_fromUtf8("dataFrame_nav_untroubled_toolbutton"))
        self.layout_dataframe_nav_left.addWidget(self.dataFrame_nav_untroubled_toolbutton)
        self.dataFrame_nav_billing_toolbutton = QtGui.QToolButton(self.dataframe_nav__frame)
        self.dataFrame_nav_billing_toolbutton.setMinimumSize(QtCore.QSize(0, 30))
        self.dataFrame_nav_billing_toolbutton.setStyleSheet(_fromUtf8("background-color:rgba(48, 48, 48, 255)"))
        self.dataFrame_nav_billing_toolbutton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.dataFrame_nav_billing_toolbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.dataFrame_nav_billing_toolbutton.setAutoRaise(True)
        self.dataFrame_nav_billing_toolbutton.setObjectName(_fromUtf8("dataFrame_nav_billing_toolbutton"))
        self.layout_dataframe_nav_left.addWidget(self.dataFrame_nav_billing_toolbutton)
        self.dataframe_nav_browser_button = QtGui.QPushButton(self.dataframe_nav__frame)
        self.dataframe_nav_browser_button.setMinimumSize(QtCore.QSize(0, 30))
        self.dataframe_nav_browser_button.setMaximumSize(QtCore.QSize(75, 16777215))
        self.dataframe_nav_browser_button.setStyleSheet(_fromUtf8("background-color:rgba(30, 30, 30, 255);"))
        self.dataframe_nav_browser_button.setFlat(True)
        self.dataframe_nav_browser_button.setObjectName(_fromUtf8("dataframe_nav_browser_button"))
        self.layout_dataframe_nav_left.addWidget(self.dataframe_nav_browser_button)
        self.dataframe_nav_console_button = QtGui.QPushButton(self.dataframe_nav__frame)
        self.dataframe_nav_console_button.setMinimumSize(QtCore.QSize(0, 30))
        self.dataframe_nav_console_button.setMaximumSize(QtCore.QSize(75, 16777215))
        self.dataframe_nav_console_button.setStyleSheet(_fromUtf8("background-color:rgba(30, 30, 30, 255);"))
        self.dataframe_nav_console_button.setFlat(True)
        self.dataframe_nav_console_button.setObjectName(_fromUtf8("dataframe_nav_console_button"))
        
        self.billingMenu_gatorbill_action = QtGui.QAction("Gatorbill",self.dataFrame_nav_billing_toolbutton)
        self.billingMenu_search_action = QtGui.QAction("Billing search",self.dataFrame_nav_billing_toolbutton)
        self.billingMenu_packageSchema_action = QtGui.QAction("Package Schema", self.dataFrame_nav_billing_toolbutton)
        
        self.dataFrame_nav_billing_toolbutton.addAction(self.billingMenu_gatorbill_action)
        self.dataFrame_nav_billing_toolbutton.addAction(self.billingMenu_search_action)
        self.dataFrame_nav_billing_toolbutton.addAction(self.billingMenu_packageSchema_action)
        
        
        self.untroubledMenu_dns_action = QtGui.QAction("DNS Troubleshooter",self.dataFrame_nav_untroubled_toolbutton)
        #self.untroubledMenu_email_action = QtGui.QAction("Email Troubleshooter",self.dataFrame_nav_untroubled_toolbutton)
        
        self.dataFrame_nav_untroubled_toolbutton.addAction(self.untroubledMenu_dns_action)
        #self.dataFrame_nav_untroubled_toolbutton.addAction(self.untroubledMenu_email_action)

        
        self.layout_dataframe_nav_left.addWidget(self.dataframe_nav_console_button)
        spacerItem1 = QtGui.QSpacerItem(286, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_dataframe_nav_left.addItem(spacerItem1)
        self.dataframe_nav_login_button = QtGui.QPushButton(self.dataframe_nav__frame)
        self.dataframe_nav_login_button.setFlat(True)
        self.dataframe_nav_login_button.setObjectName(_fromUtf8("dataframe_nav_login_button"))
        self.layout_dataframe_nav_left.addWidget(self.dataframe_nav_login_button)
        self.layout_dataframe_main.addWidget(self.dataframe_nav__frame)
        self.dataframe_body_frame = QtGui.QFrame(self.dataframe_frame_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataframe_body_frame.sizePolicy().hasHeightForWidth())
        self.dataframe_body_frame.setSizePolicy(sizePolicy)
        self.dataframe_body_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.dataframe_body_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dataframe_body_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.dataframe_body_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.dataframe_body_frame.setObjectName(_fromUtf8("dataframe_body_frame"))
        #self.dataframe_body_frame.setStyle("background-image:../resources/unt-logo-3dlds1.png")
        self.layout_dataframe_body = QtGui.QHBoxLayout(self.dataframe_body_frame)
        self.layout_dataframe_body.setSpacing(0)
        self.layout_dataframe_body.setMargin(0)
        self.layout_dataframe_body.setObjectName(_fromUtf8("layout_dataframe_body"))
        '''
        self.dataframe_body_placeholder_label = QtGui.QLabel(self.dataframe_body_frame)
        self.dataframe_body_placeholder_label.setMinimumSize(QtCore.QSize(300, 300))
        self.dataframe_body_placeholder_label.setMaximumSize(QtCore.QSize(300, 300))
        self.dataframe_body_placeholder_label.setText(_fromUtf8(""))
        self.dataframe_body_placeholder_label.setPixmap(QtGui.QPixmap(_fromUtf8("../resources/unt-logo-3dlds1.png")))
        self.dataframe_body_placeholder_label.setObjectName(_fromUtf8("dataframe_body_placeholder_label"))
        self.layout_dataframe_body.addWidget(self.dataframe_body_placeholder_label)
        '''
        self.layout_dataframe_main.addWidget(self.dataframe_body_frame)
        self.layout_content.addWidget(self.dataframe_frame_main)
        self.layout_main.addWidget(self.content_frame)
        self.status_frame = QtGui.QFrame(untroubled)
        self.status_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.status_frame.setStyleSheet(_fromUtf8("background-color:rgb(110,110,110);"))
        self.status_frame.setFrameShape(QtGui.QFrame.Panel)
        self.status_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.status_frame.setLineWidth(1)
        self.status_frame.setObjectName(_fromUtf8("status_frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.status_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.status_label = QtGui.QLabel(self.status_frame)
        self.status_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.status_label.setFrameShadow(QtGui.QFrame.Plain)
        self.status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.horizontalLayout.addWidget(self.status_label)
        self.layout_main.addWidget(self.status_frame)

        self.retranslateUi(untroubled)
        QtCore.QMetaObject.connectSlotsByName(untroubled)
        
        
        self.dashboard = QtWebKit.QWebView(self.status_frame)
        #self.dashboard.setUrl(QtCore.QUrl(_fromUtf8("http://dashboard.hostgator.com")))
        self.dashboard.setUrl(QtCore.QUrl(_fromUtf8("http://dashboard.hostgator.com")))
        self.dashboard.setObjectName(_fromUtf8("dashboard"))
        self.dashboard.resize(QtCore.QSize(1,1))  
        self.eventManager = EventManager()
        self.chats = sessionManager(self.eventManager, self.dataframe_body_frame,self.layout_dataframe_body,self.sessions_container_frame,self.dashboard)

        QtCore.QObject.connect(self.sessions_add_button, QtCore.SIGNAL("clicked()"), self.addSession)
        
        
        '''        
        self.dashboard.loadFinished.connect(self.dbLogin)
        self.chats = sessionManager.sessionManager(self.frame,self.horizontalLayout,self.listView,self.dashboard)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.startCheck)
        '''


    def retranslateUi(self, untroubled):
        untroubled.setWindowTitle(_translate("untroubled", "Form", None))
        self.sessions_add_button.setText(_translate("untroubled", "Add New", None))
        self.label.setText(_translate("untroubled", "Selected Tool", None))
        self.dataFrame_nav_billing_toolbutton.setText(_translate("untroubled", "Billing", None))
        self.dataframe_nav_browser_button.setText(_translate("untroubled", "Browser", None))
        self.dataframe_nav_console_button.setText(_translate("untroubled", "Console", None))
        self.dataframe_nav_login_button.setText(_translate("untroubled", "Log in", None))
        self.status_label.setText(_translate("untroubled", "Status", None))
        
    def addSession(self):
        pass

    '''    
    def dbLogin(self,success):
        QtCore.QTimer.singleShot(2000, self.dbLoginTrue)
        print "login fired"
        self.dashboard.page().mainFrame().addToJavaScriptWindowObject("unt", self)
        #self.dashboard.page().mainFrame().evaluateJavaScript("function check(){unt.chatCallback('hello');setTimeout(function(){check()},2000)}")
        #self.dashboard.page().mainFrame().evaluateJavaScript("check();") 
    
    def dbLoginTrue(self):
        print "logintrue fired"
        self.dashboard.page().mainFrame().addToJavaScriptWindowObject("unt", self)
        self.dashboard.page().mainFrame().evaluateJavaScript("DashboardChatWidgets.staffLogin('"+self.login[0]+"','"+self.login[1]+"')")        
        
        QtCore.QTimer.singleShot(2000, self.startCheck)


    def startCheck(self):    
        print "Updating Chats"    
        self.dashboard.page().mainFrame().evaluateJavaScript('cList = "";for(chat in DashboardChatWidgets.chats){if(DashboardChatWidgets.chats[chat].clientId > 1){DashboardChatWidgets.chats[chat].billingUrl="https://gbadmin.hostgator.com/client/"+DashboardChatWidgets.chats[chat].clientId};cList += DashboardChatWidgets.chats[chat].chatId +","+DashboardChatWidgets.chats[chat].customerName+","+DashboardChatWidgets.chats[chat].billingUrl+","+DashboardChatWidgets.chats[chat].start+"|"}')
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
    '''            
