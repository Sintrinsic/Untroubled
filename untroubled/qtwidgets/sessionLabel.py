# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sessionLabel.ui'
#
# Created: Wed Oct 23 19:20:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untroubled.event.ChatEvent import ChatEvent
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

class sessionLabel(QtGui.QWidget):
    def __init__(self, name, parent=None, chatSession=None):
        super(sessionLabel, self).__init__(parent)
        self.chatSession = chatSession
        self.setupUi(self,name)
    
    def setupUi(self, sessionLabel,name ):
        self.nameString = name
        sessionLabel.setObjectName(_fromUtf8("sessionLabel"))
        sessionLabel.resize(255, 33)
        sessionLabel.setStyleSheet(_fromUtf8("background-color:rgb(140, 140, 140)"))
        self.horizontalLayout = QtGui.QHBoxLayout(sessionLabel)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.name = QtGui.QLabel(sessionLabel)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.time = QtGui.QLabel(sessionLabel)
        self.time.setObjectName(_fromUtf8("time"))
        self.horizontalLayout.addWidget(self.time)
        self.close_button = QtGui.QPushButton(sessionLabel)
        self.close_button.setMinimumSize(QtCore.QSize(20, 0))
        self.close_button.setMaximumSize(QtCore.QSize(20, 16777215))
        self.close_button.setStyleSheet(_fromUtf8("color:red;"))
        self.close_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/icon-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.close_button.setIcon(icon)
        self.close_button.setFlat(True)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout.addWidget(self.close_button)
        self.name.setText(QtCore.QString(self.nameString))
        self.retranslateUi(sessionLabel)
        QtCore.QMetaObject.connectSlotsByName(sessionLabel)
        self.close_button.clicked.connect(self.closeSelf)

    def retranslateUi(self, sessionLabel):
        sessionLabel.setWindowTitle(_translate("sessionLabel", "Form", None))
        self.time.setText(_translate("sessionLabel", "2:10", None))

    def mousePressEvent(self, event):
        chatEvent = ChatEvent("manual_selected", self.chatSession.ID, "selected", self.chatSession)
        self.chatSession.eventHandler.call("chatEvent",chatEvent)
        

    def closeSelf(self):
        self.chatSession.remove()
        

