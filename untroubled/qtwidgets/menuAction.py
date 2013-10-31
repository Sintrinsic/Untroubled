'''
Created on Oct 30, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui
from untroubled.event.NavEvent import NavEvent

class menuAction(QtGui.QAction):
    def __init__(self, QString, QObject, eventHandler):
        super(menuAction, self).__init__(QString, QObject)
        self.eventHandler = eventHandler
    
        
    def triggered(self, bool):
        print "Nav clicked"
        navEvent = NavEvent("untroubled_nav_clicked", str(self.text()))
        self.eventManager.call("navEvent", navEvent)