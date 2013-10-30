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

from untroubled.chatSession.ChatSession import ChatSession


class sessionManager(object):

    def __init__(self,eventHandler,targetFrame,targetLayout,targetList,dashboard):
        self.dashboard = dashboard
        self.layout = targetLayout
        self.dataFrame = targetFrame
        self.listFrame = targetList
        self.eventHandler = eventHandler
        '''
        self.listView = targetList
        self.listSelector = self.listView.selectionModel()
        self.listModel = QStandardItemModel(self.listView)
        self.listView.setModel(self.listModel)
        '''
        #self.listView.selectionChanged.connect(self.selectionChanged())
        #self.list: [chatId, name,billing,starttime,dataFrameWidget,QListViewIndex]
        self.list = numpy.delete(numpy.ndarray((1,6),dtype=object),0,0)
        
        self.manualList = numpy.ndarray((1,6),dtype=object)
        self.manualList = numpy.delete(numpy.ndarray((1,6),dtype=object),0,0)
        self.addSession([0,"FakeChad","https://gbadmin.hostgator.com/client/1189034","1234567"],True)
        self.addSession([1,"Feofake Hamad","https://gbadmin.hostgator.com/client/1881256","1234567"],True)

        self.selectSession(0)

        
    def assessChats(self, current):
        if not current:
            current = numpy.delete(numpy.ndarray((1,6),dtype=object),0,0)
        current = numpy.asanyarray(current,dtype=object)

        common = numpy.intersect1d(current[0:,0],self.list[0:,0])
        if len(self.manualList) > 0:
            if len(common) >0:
                common = numpy.append(common, self.manualList[0:,0], axis=0)
            else:
                common = self.manualList
        #[self.removeSession(d) for d in self.list[self.list[0:,0]!=common]]
        for l in self.list[0:,0]:
            if l not in common:
                self.removeSession(l)

        for c in current[0:,0]:
            if c not in common:
                self.addSession(current[current[0:,0]==c][0])
            
        for c in current:
            currentUrl = c[2]
            listItem = self.list[self.list[0:,0]==c[0]][0]
            listItem[1].addBilling(currentUrl)

    def addSession(self,addArray,manual=False):
        #[id,name,billingURL,starTime]
        chatId = addArray[0]
        name = addArray[1]
        label = sessionLabel(name, self.listFrame)
        billing = addArray[2]
        startTime = addArray[3]
        newIndex = len(self.list)
        cmdExec = cmdExecutor(chatshell(),self.eventHandler)
        chatFrame = QtGui.QWidget(self.dataFrame)
        session = ChatSession(name,label, chatFrame,cmdExec)
        self.layout.addWidget(chatFrame)
        chatFrame.setVisible(False)

        chatList = [chatId,session,billing ,startTime, chatFrame,newIndex]
        if manual:
            self.manualList = numpy.append(self.manualList,[chatList],axis=0)

        self.list = numpy.append(self.list,[chatList],axis=0)
        #if ( [None]*6 in self.list):

        print newIndex
        #self.listModel.insertRow(newIndex, session)
        
    def removeSession(self,toRemove):
        print "Begin"
        print "startingArray"+str(toRemove)
        if toRemove in self.manualList[0:,0]:
            self.manualList = numpy.delete(self.manualList,toRemove,axis=0)

        self.selectSession(self.list[0,0])
        index = 0
        for listChat in self.list:
            if listChat[0] == toRemove:

                listChat[4].setVisible(False)
                listChat[4].destroy()
                self.list = numpy.delete(self.list,index,0)
                self.listModel.removeRow(listChat[5])
                self.list[self.list[0:,5]>listChat[5],5] -= 1
            index += 1
        print "Done"
        
    def selectionChanged(self,newSelection, oldSelection):
        index = newSelection.indexes()[0].row()
        print self.list[self.list[0:,5]==index]
        chat= self.list[self.list[0:,5]==index][0]
        print chat[1].text()+"Selected."
        self.selectSession(chat[0])
        
    def selectSession(self,chatId):
        [c[4].setVisible(True if c[0]==chatId else False) for c in self.list] 
        

    
        
        
        
    