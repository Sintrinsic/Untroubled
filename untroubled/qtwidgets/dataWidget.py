'''
Created on Oct 30, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui


class dataWidget(QtGui.QWidget):

    def __init__(self, parent=None, eventManager, chatID):
        super(dataWidget,self).__init__(parent)
        self.eventManager = eventManager
        self.chatID = chatID
        self.eventManager.register("chatEvent", self.selectedListener)

    def selectedListener(self, event):
        if event.eventType == "selected":
            if event.ID == self.chatID:
                self.setVisible(True)
            else:
                self.setVisible(False)
        