'''
Created on Oct 30, 2013

@author: bdupree
'''

from untroubled.event.baseEvent import BaseEvent
class NavEvent(BaseEvent):
    '''
    Event for the signaling of chats being added/removed/selected.
    '''

    def __init__(self,eventIdentifier, navOption):
        self.identifier = eventIdentifier
        self.canceled = False #Useless atm. 
        self.navOption = navOption
        