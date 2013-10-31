'''
Created on Oct 30, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui
from untroubled.qtwidgets.ConsoleWidget import ConsoleWidget

class dataWidget(QtGui.QWidget):

    def __init__(self, chatSession, parent=None, eventManager=None, chatID=0):
        super(dataWidget,self).__init__(parent)
        self.eventManager = eventManager
        self.layout = QtGui.QVBoxLayout(self)
        self.chatSession = chatSession
        self.chatID = chatID
        #self.setStyleSheet("background-color:rgb(255,255,"+str(self.chatID*50)+")")
        self.eventManager.register("chatEvent", self.selectedListener)
        self.eventManager.register("navEvent", self.navListener)
        self.selected = False
        self.widgets = {}
        self.activeWidget = None
        self.addWidget("Gatorbill", self.chatSession.billingBrowser)
        self.addWidget("console", ConsoleWidget(self.chatSession) )
        self.setActiveWidget("Gatorbill")

    def selectedListener(self, event):
        if event.eventType == "selected":
            if event.chatID == self.chatID:
                self.setVisible(True)
                self.selected = True
                self.activeWidget.setVisible(True)

                print "Chat ID "+str(self.chatID)+" selected."
            else:
                self.setVisible(False)
                self.selected = False
                
    def navListener(self, event):
        if self.selected:
            print "Nav option "+event.navOption+" clicked for chat ID: "+str(self.chatID)
            
    def addWidget(self, name, widget):
        self.widgets[name] = widget
        widget.setParent(self)
        self.layout.addWidget(widget)
        widget.setVisible(False)
        
            
    def setActiveWidget(self, name):
        if self.activeWidget != None:
            self.activeWidget.setVisible(False)
        self.activeWidget = self.widgets[name]
        self.activeWidget.setVisible(True)
        