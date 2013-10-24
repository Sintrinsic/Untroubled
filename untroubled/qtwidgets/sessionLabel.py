# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sessionLabel.ui'
#
# Created: Wed Oct 23 19:20:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_sessionLabel(object):
    def setupUi(self, sessionLabel):
        sessionLabel.setObjectName(_fromUtf8("sessionLabel"))
        sessionLabel.resize(255, 33)
        sessionLabel.setStyleSheet(_fromUtf8("background-color:rgb(140, 140, 140)"))
        self.horizontalLayout = QtGui.QHBoxLayout(sessionLabel)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.name = QtGui.QLineEdit(sessionLabel)
        self.name.setFrame(False)
        self.name.setReadOnly(True)
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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Pictures/icon-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setFlat(True)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout.addWidget(self.close_button)

        self.retranslateUi(sessionLabel)
        QtCore.QMetaObject.connectSlotsByName(sessionLabel)

    def retranslateUi(self, sessionLabel):
        sessionLabel.setWindowTitle(_translate("sessionLabel", "Form", None))
        self.name.setText(_translate("sessionLabel", "Fakechat 1", None))
        self.time.setText(_translate("sessionLabel", "2:10", None))

