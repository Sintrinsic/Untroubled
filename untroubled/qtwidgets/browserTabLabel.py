# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sessionLabel.ui'
#
# Created: Wed Oct 23 19:20:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untroubled.event.genericEvent import GenericEvent
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

class browserTabLabel(QtGui.QWidget):
    def __init__(self, browser, id, chatSession, parent=None):
        super(browserTabLabel, self).__init__(parent)
        self.chatSession = chatSession
        self.browser = browser
        self.ID = id
        self.nameString = "New Tab"

        self.setupUi(self)
    
    def setupUi(self, tabLabel):
        tabLabel.setObjectName(_fromUtf8("tabLabel"))
        tabLabel.resize(255, 33)
        tabLabel.setStyleSheet(_fromUtf8("background-color:rgb(140, 140, 140)"))
        self.horizontalLayout = QtGui.QHBoxLayout(tabLabel)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout.setMargin(1)
        self.horizontalLayout.setSpacing(0)
        self.name = QtGui.QLabel(tabLabel)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.close_button = QtGui.QPushButton(tabLabel)
        self.close_button.setMinimumSize(QtCore.QSize(20, 0))
        self.close_button.setMaximumSize(QtCore.QSize(20, 16777215))
        self.close_button.setStyleSheet(_fromUtf8("color:red;"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/icon-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.close_button.setIcon(icon)
        self.close_button.setFlat(True)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout.addWidget(self.close_button)
        self.name.setText(QtCore.QString(self.nameString))
        QtCore.QMetaObject.connectSlotsByName(tabLabel)
        self.close_button.clicked.connect(self.closeSelf)
        self.chatSession.eventHandler.register(str(self.ID)+"_browserNav",self.selected)
        self.browser.loadFinished.connect(self.urlChanged)

    def mousePressEvent(self, event):
        print "browser tab selected"
        chatEvent = GenericEvent("tab_selected",{"action":"selected","browser":self.browser,"ID":self.chatSession.ID})
        eventTypeString = str(self.ID)+"_browserNav"
        self.chatSession.eventHandler.call(eventTypeString, chatEvent)
        
    def selected(self, event):
        print "browser tab selected: event hit"
        if event.meta["action"] == "selected" and event.meta["browser"].ID == self.browser.ID:
            self.setStyleSheet(_fromUtf8("background-color:rgb(180, 180, 180)"))
            print self.ID
        else:
            self.setStyleSheet(_fromUtf8("background-color:rgb(160, 160, 160)"))

    def urlChanged(self):
        title = str(self.browser.page().mainFrame().title())
       
        self.name.setText(title)    
        
    def closeSelf(self):
        self.chatSession.remove()
        

