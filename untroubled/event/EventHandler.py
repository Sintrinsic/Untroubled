'''
Created on Oct 26, 2013

@author: sintrinsic
'''
import time
from PyQt4 import QtCore, QtGui

class eventManager(object):
    '''
    Handler for the registration and the distribution of events to registered listeners. 
    EventHandlers will be in format:
    def method(self, event)
    '''


    def __init__(self):
        self.handlerList = {}
        self.asyncQueue = []
        self.locked = False
        
        
    def register(self, eventName, callbackMethod):
        if not eventName in self.handlerList.keys():
            print "Event "+eventName+" does not exist. Creating."
            self.handlerList[eventName] = []
        if not callbackMethod in self.handlerList[eventName]:
            self.handlerList[eventName].append(callbackMethod)
    
    def unregister(self, eventName, callbackMethod):
        if callbackMethod in self.handlerList[eventName]:
            self.handlerList[eventName].remove(callbackMethod)
            
    def call(self, eventName, event):
        while self.locked:
            time.sleep(.1)
        self.locked = True
        self.asyncQueue.append([eventName, event])
        self.locked = False
        
    def runQueue(self):
        if not self.locked:
            self.locked = True
            for e in self.asyncQueue:
                self.__call(e[0], e[1])
            self.asyncQueue = []
            self.locked = False

        
    def __call(self, eventName, event):
        for h in self.handlerList[eventName]:
            #need exception handling here
            h(event)
        