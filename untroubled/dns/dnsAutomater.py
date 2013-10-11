# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dnsAutomater.ui'
#
# Created: Wed Oct  9 17:03:57 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untroubled.data.cmdParser import cmdExecutor
from untroubled.dns import vZoneLocal, vZoneRemote
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

class Ui_frame(QtGui.QFrame):
    def __init__(self,parent):
        super(Ui_frame,self).__init__(parent)
        self.setupUi(parent)
        self.cmdExecutor = cmdExecutor("bob")
        
    def setupUi(self, frame_main):
        parent = frame_main
        frame_main = QtGui.QFrame(parent)
        
        frame_main.setObjectName(_fromUtf8("frame_main"))
        frame_main.resize(846, 523)
        frame_main.setFrameShape(QtGui.QFrame.StyledPanel)
        frame_main.setFrameShadow(QtGui.QFrame.Raised)
        
        self.layout_main = QtGui.QVBoxLayout(frame_main)
        self.layout_main.setSpacing(0)
        self.layout_main.setMargin(0)
        self.layout_main.setObjectName(_fromUtf8("layout_main"))
        self.frame_text = QtGui.QFrame(frame_main)
        self.frame_text.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_text.setObjectName(_fromUtf8("frame_text"))
        self.layout_text = QtGui.QHBoxLayout(self.frame_text)
        self.layout_text.setMargin(0)
        self.layout_text.setObjectName(_fromUtf8("layout_text"))
        self.lineEdit = QtGui.QLineEdit(self.frame_text)
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.layout_text.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.frame_text)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layout_text.addWidget(self.pushButton)
        self.layout_main.addWidget(self.frame_text)
        self.frame_contents = QtGui.QFrame(frame_main)
        self.frame_contents.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_contents.setObjectName(_fromUtf8("frame_contents"))
        self.layout_contents = QtGui.QHBoxLayout(self.frame_contents)
        self.layout_contents.setSpacing(0)
        self.layout_contents.setMargin(0)
        self.layout_contents.setObjectName(_fromUtf8("layout_contents"))
        self.tabWidget = QtGui.QTabWidget(self.frame_contents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layout_tab = QtGui.QHBoxLayout(self.tab)
        self.layout_tab.setObjectName(_fromUtf8("layout_tab"))
        self.frame_tab_left = QtGui.QFrame(self.tab)
        self.frame_tab_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_tab_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tab_left.setObjectName(_fromUtf8("frame_tab_left"))
        self.layout_tab_left = QtGui.QHBoxLayout(self.frame_tab_left)
        self.layout_tab_left.setObjectName(_fromUtf8("layout_tab_left"))
        self.textBrowser_left = QtGui.QTextBrowser(self.frame_tab_left)
        self.textBrowser_left.setObjectName(_fromUtf8("textBrowser_left"))
        self.layout_tab_left.addWidget(self.textBrowser_left)
        self.layout_tab.addWidget(self.frame_tab_left)
        self.frame_tab_right = QtGui.QFrame(self.tab)
        self.frame_tab_right.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_tab_right.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_tab_right.setObjectName(_fromUtf8("frame_tab_right"))
        self.layout_tab_right = QtGui.QHBoxLayout(self.frame_tab_right)
        self.layout_tab_right.setObjectName(_fromUtf8("layout_tab_right"))
        self.textBrowser_right = QtGui.QTextBrowser(self.frame_tab_right)
        self.textBrowser_right.setObjectName(_fromUtf8("textBrowser_right"))
        self.layout_tab_right.addWidget(self.textBrowser_right)
        self.layout_tab.addWidget(self.frame_tab_right)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.layout_contents.addWidget(self.tabWidget)
        self.layout_main.addWidget(self.frame_contents)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.doDNS)

        self.retranslateUi(frame_main)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frame_main)

    def retranslateUi(self, frame_main):
        frame_main.setWindowTitle(_translate("frame_main", "Frame", None))
        self.pushButton.setText(_translate("frame_main", "PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frame_main", "Tab 1", None))



    def doDNS(self):
        domain = str(self.lineEdit.text())
        widget = QtGui.QWidget(self.tabWidget)     
        widget.setObjectName(_fromUtf8("widget_"+domain))
        horizontalLayout = QtGui.QHBoxLayout(widget)
        horizontalLayout.setSpacing(0)
        horizontalLayout.setMargin(0)
        horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"+domain))
        widget.setLayout(horizontalLayout)
        textBoxL = QtGui.QTextBrowser(widget)
        textBoxR = QtGui.QTextBrowser(widget)
        horizontalLayout.addWidget(textBoxL)
        horizontalLayout.addWidget(textBoxR)
        vzR = vZoneRemote.vZoneRemote(domain)
        vzL = vZoneLocal.vZoneLocal(open("dns/zt1").read(),domain,self.cmdExecutor)
        textBoxL.setText(vzL.printRecords())
        textBoxR.setText(vzR.printRecords())
        self.tabWidget.addTab(widget, QtCore.QString(domain))
        
        
