# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browserWidget2.ui'
#
# Created: Thu Oct 31 19:36:52 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit
from untroubled.qtwidgets.browserTabLabel import browserTabLabel

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

class browserWidget(QtGui.QWidget):
    def __init__(self,chatSession,parent=None):
        super(browserWidget, self).__init__(parent)
        self.tabCount = 0
        self.chatSession = chatSession
        self.setupUi(self)


    
    def setupUi(self, mainWidget):
        self.layout_main = QtGui.QHBoxLayout(mainWidget)
        self.layout_main.setSpacing(0)
        self.layout_main.setMargin(0)
        self.layout_main.setObjectName(_fromUtf8("layout_main"))
        self.mainFrame = QtGui.QFrame(mainWidget)
        self.mainFrame.setStyleSheet(_fromUtf8("background-color:rgb(170, 170, 170)"))
        self.mainFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.layout_mainFrame = QtGui.QVBoxLayout(self.mainFrame)
        self.layout_mainFrame.setSpacing(0)
        self.layout_mainFrame.setMargin(0)
        self.layout_mainFrame.setObjectName(_fromUtf8("layout_mainFrame"))
        self.navFrame = QtGui.QFrame(self.mainFrame)
        self.navFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.navFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.navFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.navFrame.setObjectName(_fromUtf8("navFrame"))
        self.layout_nav = QtGui.QHBoxLayout(self.navFrame)
        self.layout_nav.setSpacing(0)
        self.layout_nav.setMargin(0)
        self.layout_nav.setObjectName(_fromUtf8("layout_nav"))
        self.navBack_button = QtGui.QToolButton(self.navFrame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/backward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navBack_button.setIcon(icon)
        self.navBack_button.setObjectName(_fromUtf8("navBack_button"))
        self.layout_nav.addWidget(self.navBack_button)
        self.navForward_button = QtGui.QToolButton(self.navFrame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navForward_button.setIcon(icon1)
        self.navForward_button.setObjectName(_fromUtf8("navForward_button"))
        self.layout_nav.addWidget(self.navForward_button)
        self.navUrl_textEdit = QtGui.QLineEdit(self.navFrame)
        self.navUrl_textEdit.setStyleSheet(_fromUtf8("background-color:none"))
        self.navUrl_textEdit.setObjectName(_fromUtf8("navUrl_textEdit"))
        self.layout_nav.addWidget(self.navUrl_textEdit)
        self.navReload_button = QtGui.QToolButton(self.navFrame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navReload_button.setIcon(icon2)
        self.navReload_button.setIconSize(QtCore.QSize(16, 16))
        self.navReload_button.setObjectName(_fromUtf8("navReload_button"))
        self.layout_nav.addWidget(self.navReload_button)
        self.layout_mainFrame.addWidget(self.navFrame)
        self.hotbar_frame = QtGui.QFrame(self.mainFrame)
        self.hotbar_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hotbar_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.hotbar_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.hotbar_frame.setObjectName(_fromUtf8("hotbar_frame"))
        self.layout_hotbar = QtGui.QHBoxLayout(self.hotbar_frame)
        self.layout_hotbar.setMargin(0)
        self.layout_hotbar.setObjectName(_fromUtf8("layout_hotbar"))
        self.hotbar_tools_linksbutton = QtGui.QToolButton(self.hotbar_frame)
        self.hotbar_tools_linksbutton.setMinimumSize(QtCore.QSize(60, 0))
        self.hotbar_tools_linksbutton.setObjectName(_fromUtf8("hotbar_tools_linksbutton"))
        self.layout_hotbar.addWidget(self.hotbar_tools_linksbutton)
        self.hotbar_links2_toolButton = QtGui.QToolButton(self.hotbar_frame)
        self.hotbar_links2_toolButton.setMinimumSize(QtCore.QSize(60, 0))
        self.hotbar_links2_toolButton.setObjectName(_fromUtf8("hotbar_links2_toolButton"))
        self.layout_hotbar.addWidget(self.hotbar_links2_toolButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_hotbar.addItem(spacerItem)
        self.hotbar_tools_toolButton1 = QtGui.QToolButton(self.hotbar_frame)
        self.hotbar_tools_toolButton1.setObjectName(_fromUtf8("hotbar_tools_toolButton1"))
        self.layout_hotbar.addWidget(self.hotbar_tools_toolButton1)
        self.layout_mainFrame.addWidget(self.hotbar_frame)
        self.tabsFrame = QtGui.QFrame(self.mainFrame)
        self.tabsFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.tabsFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.tabsFrame.setObjectName(_fromUtf8("tabsFrame"))
        self.layout_tabsFrame = QtGui.QVBoxLayout(self.tabsFrame)
        self.layout_tabsFrame.setSpacing(0)
        self.layout_tabsFrame.setMargin(0)
        self.layout_tabsFrame.setObjectName(_fromUtf8("layout_tabsFrame"))
        self.content_frame = QtGui.QFrame(self.tabsFrame)
        self.content_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.content_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.content_frame.setObjectName(_fromUtf8("content_frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.content_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabs_frame = QtGui.QFrame(self.content_frame)
        self.tabs_frame.setMinimumSize(QtCore.QSize(150, 0))
        self.tabs_frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tabs_frame.setStyleSheet(_fromUtf8("background-color:rgb(140, 140, 140)"))
        self.tabs_frame.setFrameShape(QtGui.QFrame.Panel)
        self.tabs_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.tabs_frame.setObjectName(_fromUtf8("tabs_frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabs_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.tabs_container_frame = QtGui.QFrame(self.tabs_frame)
        self.tabs_container_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.tabs_container_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.tabs_container_frame.setObjectName(_fromUtf8("tabs_container_frame"))
        self.tabs_container_frame.setStyleSheet(QtCore.QString("background-color:none"))
        self.verticalLayout.addWidget(self.tabs_container_frame)
        self.layout_tabs_container = QtGui.QVBoxLayout(self.tabs_container_frame)
        self.layout_tabs_container.setSpacing(0)
        self.layout_tabs_container.setMargin(0)
        self.tabs_add_frame = QtGui.QWidget(self.tabs_frame)
        self.tabs_add_frame.setMinimumSize(QtCore.QSize(0, 25))
        self.tabs_add_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tabs_add_frame.setObjectName(_fromUtf8("tabs_add_frame"))
        self.layout_tabs_add_frame = QtGui.QVBoxLayout(self.tabs_add_frame)#-------------------------------------
        self.layout_tabs_add_frame.setSpacing(0)
        self.layout_tabs_add_frame.setMargin(0)

        '''
        self.tabs_add_label = QtGui.QLabel(self.tabs_add_frame)
        self.tabs_add_label.setMinimumSize(QtCore.QSize(16, 16))
        self.tabs_add_label.setMaximumSize(QtCore.QSize(16, 16))
        self.tabs_add_label.setBaseSize(QtCore.QSize(18, 18))
        self.tabs_add_label.setText(_fromUtf8(""))
        self.tabs_add_label.setPixmap(QtGui.QPixmap(_fromUtf8("../resources/add.png")))
        self.tabs_add_label.setScaledContents(True)
        self.tabs_add_label.setWordWrap(False)
        self.tabs_add_label.setObjectName(_fromUtf8("tabs_add_label"))
        self.horizontalLayout_2.addWidget(self.tabs_add_label)
        '''
        self.tabs_add_button = QtGui.QPushButton(self.tabs_add_frame)
        self.tabs_add_button.setMinimumSize(QtCore.QSize(0, 25))
        self.tabs_add_button.setStyleSheet(_fromUtf8("background-color:rgb(150, 150, 150)"))
        self.tabs_add_button.setFlat(False)
        addIcon = QtGui.QIcon(QtGui.QPixmap(_fromUtf8("../resources/add.png")))
        self.tabs_add_button.setIcon(addIcon)
        self.tabs_add_button.setObjectName(_fromUtf8("tabs_add_button"))
        self.layout_tabs_add_frame.addWidget(self.tabs_add_button)
        self.verticalLayout.addWidget(self.tabs_add_frame)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.tabs_frame)
        self.page_frame = QtGui.QFrame(self.content_frame)
        self.page_frame.setFrameShape(QtGui.QFrame.Panel)
        self.page_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.page_frame.setLineWidth(1)
        self.page_frame.setObjectName(_fromUtf8("page_frame"))
        self.layout_page = QtGui.QHBoxLayout(self.page_frame)
        self.horizontalLayout.addWidget(self.page_frame)
        self.layout_tabsFrame.addWidget(self.content_frame)
        self.status_frame = QtGui.QFrame(self.tabsFrame)
        self.status_frame.setMinimumSize(QtCore.QSize(0, 25))
        self.status_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.status_frame.setStyleSheet(_fromUtf8(""))
        self.status_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.status_frame.setLineWidth(1)
        self.status_frame.setObjectName(_fromUtf8("status_frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.status_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.status_label_right_2 = QtGui.QLabel(self.status_frame)
        self.status_label_right_2.setObjectName(_fromUtf8("status_label_right_2"))
        self.horizontalLayout_3.addWidget(self.status_label_right_2)
        self.status_label_right = QtGui.QLabel(self.status_frame)
        self.status_label_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_label_right.setObjectName(_fromUtf8("status_label_right"))
        self.horizontalLayout_3.addWidget(self.status_label_right)
        self.layout_tabsFrame.addWidget(self.status_frame)
        self.layout_mainFrame.addWidget(self.tabsFrame)
        self.layout_main.addWidget(self.mainFrame)
        self.addTab()
        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)
        
        ''' Custon stuff '''
        self.chatSession.eventHandler.register("navEvent", self.navResponse)
        self.tabs_add_button.clicked.connect(self.addTab)
        self.navUrl_textEdit.returnPressed.connect(self.setUrl)
        self.navReload_button.clicked.connect(self.reload)
        self.navBack_button.clicked.connect(self.back)
        self.navForward_button.clicked.connect(self.forward)
        eventTypeString = str(self.chatSession.ID)+"_browserNav"
        self.chatSession.eventHandler.register(eventTypeString,self.navBrowserChangeListener)




    def setUrl(self):
        self.activeTab.customSetUrl(str(self.navUrl_textEdit.text()))
        
    def back(self):
        self.activeTab.customGoBack()
        
    def forward(self):
        self.activeTab.customGoForward()
        
    def reload(self):
        self.activeTab.customReload()
    
    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(_translate("mainWidget", "Form", None))
        self.navBack_button.setText(_translate("mainWidget", "<", None))
        self.navForward_button.setText(_translate("mainWidget", ">", None))
        self.navReload_button.setText(_translate("mainWidget", "O", None))
        self.hotbar_tools_linksbutton.setText(_translate("mainWidget", "...", None))
        self.hotbar_links2_toolButton.setText(_translate("mainWidget", "...", None))
        self.hotbar_tools_toolButton1.setText(_translate("mainWidget", "Tools", None))
        self.status_label_right_2.setText(_translate("mainWidget", "TextLabel", None))
        self.status_label_right.setText(_translate("mainWidget", "TextLabel", None))
        
    def navResponse(self, event):
        if self.chatSession.dataWidget.selected:
            if event.navOption == "browser":
                self.setVisible(True)
            else: 
                self.setVisible(False)
                
    def addTab(self):
        browser = BrowserWebView(self.chatSession, self.tabCount, self)
        browser.setVisible(False)
        tab = browserTabLabel(browser,self.chatSession.ID,self.chatSession, self)
        self.layout_page.addWidget(browser)
        self.layout_tabs_container.addWidget(tab)
        tab.mousePressEvent(None)
        self.tabCount +=1
        
    def navBrowserChangeListener(self,event):
        self.navUrl_textEdit.setText(event.meta["browser"].url().toString())
        

        
                
                
                
class BrowserWebView(QtWebKit.QWebView):

    def __init__(self, chatSession, ID, parent=None):
        super(BrowserWebView,self).__init__(parent)
        self.ID = ID
        self.browserWidget = parent
        self.chatSession = chatSession
        self.setUrl(QtCore.QUrl(QtCore.QString("http://google.com")))
        self.setStyleSheet(QtCore.QString("background-color:none;"))
        eventTypeString = str(self.chatSession.ID)+"_browserNav"
        self.chatSession.eventHandler.register(eventTypeString,self.__tabNavListner)
        self.urlChanged.connect

        
    ''' placeholders for custom interaction-triggered extra code '''
    def customSetUrl(self, urlString):
        if "http" not in urlString:
            urlString = "http://"+urlString
        url = QtCore.QUrl(QtCore.QString(urlString))
        print "URL changed to "+ urlString
        self.setUrl(url)
    
    def customGoBack(self):
        self.back()
    
    def customGoForward(self):
        self.forward()
        
    def customReload(self):
        self.reload()
        
    def updateUrl(self):
        if self.isVisible():
            self.browserWidget.navUrl_textEdit.setText(self.url().toString())
    
        
    def __tabNavListner(self,event):
        if event.meta["action"] == "selected":
            if event.meta["browser"] == self:
                self.setVisible(True)
                self.browserWidget.activeTab = self
            else:
                self.setVisible(False)
            
        
    
    

        
        
