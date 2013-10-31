'''
Created on Oct 30, 2013

@author: bdupree
'''

from untroubled.event.baseEvent import BaseEvent
class ChatEvent(BaseEvent):
    '''
    Event for the signaling of chats being added/removed/selected.
    '''

    def __init__(self,eventIdentifier, chatID, eventType, chatSession):
        self.identifier = eventIdentifier
        self.canceled = False #Useless atm. 
        self.chatID = chatID
        self.eventType = eventType #add,remove,selected
        self.session = chatSession
        
        