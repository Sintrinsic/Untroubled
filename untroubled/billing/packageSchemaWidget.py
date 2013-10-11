'''
Created on Oct 11, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui,QtHelp
from PyQt4.QtWebKit import QWebView as QWebView
import sys


class packageSchemaWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(packageSchemaWidget,self).__init__(parent)
        self.setupUi(self)
        
    
    def setupUi(self, Form):
        Form.setObjectName("MainWindow")
        Form.resize(1039, 644)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainLayout = QtGui.QHBoxLayout(Form)
        self.treeFrame = QtGui.QFrame(Form)
        self.infoFrame = QtGui.QFrame(Form)
        
        
        
        self.treeFrame_layout = QtGui.QVBoxLayout(self.treeFrame)
        self.infoFrame_layout = QtGui.QVBoxLayout(self.infoFrame)
              
        self.mainLayout.addWidget(self.treeFrame)
        self.mainLayout.addWidget(self.infoFrame)

        self.infoDisplay = QtGui.QTextBrowser(self.infoFrame)
        self.treeFrame_treeView = QtGui.QTreeWidget(self.treeFrame)
        
        
        self.infoFrame_layout.addWidget(self.infoDisplay)
        self.treeFrame_layout.addWidget(self.treeFrame_treeView)
        
        topItem = QtGui.QTreeWidgetItem(QtCore.QStringList("Top"))
        self.treeFrame_treeView.addTopLevelItem(topItem)
        topItem.addChild(QtGui.QTreeWidgetItem(QtCore.QStringList("bob")))

        topItem1 = QtGui.QTreeWidgetItem(QtCore.QStringList("Top1"))
        self.treeFrame_treeView.addTopLevelItem(topItem1)
        temp = QtGui.QTreeWidgetItem(QtCore.QStringList("Child 0"))
        topItem1.addChild(temp)
        for i in range(10):
            item = QtGui.QTreeWidgetItem(QtCore.QStringList("Child "+str(i)))
            temp.addChild(item)
            temp = item
        
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    unt = QtGui.QMainWindow()

    gui = packageSchemaWidget(unt)
    gui.setupUi(unt)
    unt.show()
    
    sys.exit(app.exec_())