'''
Created on Oct 31, 2013

@author: bdupree
'''

from PyQt4 import QtCore, QtGui
class ConsoleWidget(QtGui.QWidget):

    def __init__(self, chatSession, parent=None):
        super(ConsoleWidget,self).__init__(parent)
        self.chatSession = chatSession
        self.setObjectName(QtCore.QString("consoleWidget"))
        self.setStyleSheet("background-color:black;color:lime;font-family:monospace;font-weight:bold;")
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setObjectName(QtCore.QString("textBrowser"))
        self.textBrowser.setReadOnly(True)
        self.input = QtGui.QLineEdit(self)
        self.input.setObjectName(QtCore.QString("input"))
        self.layout.addWidget(self.textBrowser)
        self.layout.addWidget(self.input)
        self.chatSession.eventHandler.register("navEvent", self.navResponse)
        self.input.returnPressed.connect(self.sendCmd)
        self.chatSession.eventHandler.register("cmdEvent",self.getCmd)
        
    def navResponse(self, event):
        if self.chatSession.dataWidget.selected:
            if event.navOption == "console":
                self.setVisible(True)
            else: 
                self.setVisible(False)
                
                
    def sendCmd(self):
        self.textBrowser.append("superShell$ "+str(self.input.text()))
        self.chatSession.cmdExecutor.runCommandAsync(str(self.input.text()), str(self.chatSession.ID)+"_manual")
        self.input.clear()
    
    def getCmd(self, event):
        if str(self.chatSession.ID) in event.identifier:
            self.textBrowser.append(QtCore.QString(event.response))
            