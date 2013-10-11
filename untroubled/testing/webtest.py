# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webtest.ui'
#
# Created: Fri Oct  4 21:17:54 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtWebKit import QWebView
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame)
        self.QWebView = QWebView(self.centralwidget)
        self.QWebView.setUrl(QtCore.QUrl(_fromUtf8("http://dashboard.hostgator.com/")))
        self.QWebView.setObjectName(_fromUtf8("QWebView"))
        self.verticalLayout.addWidget(self.QWebView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.QWebView.page().mainFrame().addToJavaScriptWindowObject("unt", self)
        self.QWebView.page().mainFrame().evaluateJavaScript("function lp(){unt.changeButton(hc);setTimeout(function(){lp()},2000)};lp();")

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.runJS)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        
    def runJS(self):
        self.QWebView.page().mainFrame().evaluateJavaScript(self.lineEdit.text())
    
    @QtCore.pyqtSlot(str)     
    def changeButton(self,msg):
        print msg
        self.pushButton.setText(msg)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    unt = QtGui.QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(unt)
    unt.show()
    
    sys.exit(app.exec_())


