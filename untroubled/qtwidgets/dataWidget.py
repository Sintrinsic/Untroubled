'''
Created on Oct 30, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui


class dataWidget(QtGui.QWidget):

    def __init__(self, parent=None, eventManager=None, chatID=0):
        super(dataWidget,self).__init__(parent)
        self.eventManager = eventManager
        self.chatID = chatID
        self.eventManager.register("chatEvent", self.selectedListener)
        self.eventManager.register("navEvent", self.navListener)
        self.selected = False

    def selectedListener(self, event):
        if event.eventType == "selected":
            if event.chatID == self.chatID:
                self.setVisible(True)
                self.selected = True
            else:
                self.setVisible(False)
                self.selected = False
                
    def navListener(self, event):
        if self.selected:
            print "Nav option "+event.navOption+" clicked for chat ID: "+str(self.chatID)
        