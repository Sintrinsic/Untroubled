'''
Created on Oct 27, 2013

@author: bdupree
'''
from untroubled.event.baseEvent import BaseEvent
class commandEvent(BaseEvent):
    '''
    Event for the dispatch of command responses
    '''

    def __init__(self,eventIdentifier, originalCommand, response):
        self.identifier = eventIdentifier
        self.canceled = False #Useless atm. 
        self.response = response
        self.originalCommand = originalCommand

        