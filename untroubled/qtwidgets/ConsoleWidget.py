'''
Created on Oct 31, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui
class ConsoleWidget(QtGui.QWidget):

    def __init__(self, chatSession, parent=None):
        super(ConsoleWidget,self).__init__(parent)
        self.chatSession = chatSession
        self.setStyleSheet("background-color:black;color:lime;font-weight:bold;")
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setReadOnly(True)
        self.input = QtGui.QLineEdit(self)
        self.layout.addWidget(self.textBrowser)
        self.layout.addWidget(self.input)
        self.chatSession.eventHandler.register("navEvent", self.navResponse)
        self.input.returnPressed.connect(self.sendCmd)
        self.chatSession.eventHandler.register("commandEvent",self.getCmd)
        
    def navResponse(self, event):
        if self.chatSession.dataWidget.selected:
            if event.navOption == "console":
                self.setVisible(True)
            else: 
                self.setVisible(False)
                
                
    def sendCmd(self):
        self.textBrowser.append(str(self.input.text())+"\n")
    
    def getCmd(self, event):
        if str(self.chatSession.chatID) in event.identifier:
            self.textBrowser.append(QtCore.QString(event.response))
            