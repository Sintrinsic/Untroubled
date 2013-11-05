'''
Created on Nov 4, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui, QtWebKit
from untroubled.qtwidgets.browserTabLabel import browserTabLabel

class browserTab(QtGui.QWidget):


    def __init__(self, eventHandler, id, parent=None):
        super(browserTab, self).__init__(parent)
        self.eventHandler = eventHandler
        self.ID = id
        self.browser = QtWebKit.QWebView()
        label = browserTabLabel(self, self.browser, self.ID)
        
        