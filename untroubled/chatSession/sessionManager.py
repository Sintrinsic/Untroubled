'''
Created on Oct 5, 2013

@author: sintrinsic
'''
import numpy
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QStandardItemModel, QStandardItem
from PyQt4.QtCore import QObject
from untroubled.remoteCommands.cmdExecutor import cmdExecutor
from untroubled.remoteCommands.chatshell import chatshell
from untroubled.qtwidgets.sessionLabel import sessionLabel
from untroubled.event.ChatEvent import ChatEvent
from untroubled.chatSession.ChatSession import ChatSession


class sessionManager(object):

    def __init__(self,eventHandler):
        self.eventHandler = eventHandler
        self.chatIDs = {}
   
    def assessChats(self, chatList):
        currentIDs = [currentID[0] for currentID in chatList]
        new = [filter(lambda c: c[0] not in self.chatIDs) for currentID in chatList]
        old = [filter(lambda c: c not in currentIDs) for chat in self.chatIDs]
    
        for chat in new:
            self.addSession(chat)
            
        for ID in old:
            self.removeSession(ID)
        
    def addSession(self, chat):
        newSession = ChatSession(chat[1], chat[2], cmdExecutor(chatshell()),self.eventHandler)
        chatEvent = ChatEvent("sessionManager_add", chat[0], "add", newSession)
        self.eventHandler.call("chatEvent",chatEvent)
        self.chatIDs[chat[0]] = newSession
        
    def removeSession(self, ID):
        chatEvent = ChatEvent("sessionManager_remove", ID, "remove", self.chatIDs.pop(ID))
        self.eventHandler.call("chatEvent",chatEvent)
        

    