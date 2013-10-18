'''
Created on Oct 13, 2013

@author: bdupree
'''
from PyQt4 import QtCore, QtGui, QtWebKit

class billingAccount(QtCore.QObject):
    '''
    Contains all the non-sensitive information for a billing account
    Gets the owner name, primary email, account status
    '''

    def __init__(self, url, document):
        super(billingAccount,self).__init__()
        self.url = url
        self.page = document       
        self.packages = {} # {"Package name":[package],..} 
        self.invoices = []
        self.html = ""
        self.htmlCached = False
        QtCore.QTimer.singleShot(1000, self.cacheHtml)

    def cacheHtml(self):
        self.page.addToJavaScriptWindowObject("billingAccount", self)
        self.page.evaluateJavaScript("pb = $('#contact_info div[id$=div]').html();billingAccount.getElements(pb)")        
        if not self.htmlCached:
            QtCore.QTimer.singleShot(1000, self.cacheHtml)
    
    @QtCore.pyqtSlot(str)        
    def getElements(self, documentBody):
        if len(documentBody)> 10 and not self.htmlCached:
            print self.url+" HTML BODY:"
            self.html = documentBody
            #print self.html
            self.htmlCached = True
        