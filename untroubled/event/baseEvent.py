'''
Created on Oct 28, 2013

@author: bdupree
'''

class BaseEvent(object):

    def __init__(self, eventIdentifier):
        self.sender = eventIdentifier
        self.canceled = False #Useless atm. 
    