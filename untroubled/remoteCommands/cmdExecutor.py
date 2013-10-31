'''
Created on Sep 29, 2013

@author: bdupree
'''
import shlex, commands, time
import thread
from untroubled.event import commandEvent
from untroubled.event.EventManager import EventManager
from untroubled.remoteCommands.chatshell import chatshell

class cmdExecutor(object):
    '''
    Takes a command string, splits it into its individual commands and what is done with stdout (piped/to file/closed).
    If a command is a chatshell command, it's run through chatshell, and the output is put into a string and echoed for piping/printing. 
    Final product bash command is run from the local terminal, and the output is returned. 
    Note: removing all entries from untroubled.remoteCommands.commandlist makes all commands go to the local terminal. 
    '''

    def __init__(self,eventHandler):
        self.eventHandler = eventHandler
        self.breakers = ["|",";",">"]
        cmdstr = open('remoteCommands/commandList').read()
        self.cmds = cmdstr.split("\n")
        self.chatshell = False
        thread.start_new_thread(self.__getChatshell, ())

        
    def runCommand(self, cmdStr): ## --------- DEPRICATED. phasing out  ----------
        bashCommand = self.parseCommands(cmdStr)
        #cmdArray = shlex.split(bashCommand)
        output = commands.getoutput(bashCommand)
        return output
    
    def runCommandAsync(self, cmdStr, identifier):
        while self.chatshell == False:
            time.sleep(.5)
        thread.start_new_thread(self.__asyncCmdEventCaller, (cmdStr, identifier))
        
    def __asyncCmdEventCaller(self, cmdStr, identifier):
        resp = self.runCommand(cmdStr)
        event = commandEvent(identifier, cmdStr, resp)
        self.eventHandler.call("cmdEvent", event)
    
    def __getChatshell(self):
        self.chatshell = chatshell()
        
    def parseCommands(self, cmdStr):
        '''
        Parses command string into elements, converts chatshell command output to echo commands, and returns the final bash command. 
        '''
        cmdList = []
        escaped = 0
        quoted = False
        tempString = ""
        for i in cmdStr:
            
            if (i == '"' or i == "'") and (escaped < 1):
                quoted = not quoted
                
            if i == "\\" and (escaped < 1):
                escaped = 2
    
            if i in self.breakers and not quoted:
                cmdArray = self.getCmdElements(tempString, i)
                cmdList.append(cmdArray)
                tempString = ""
                continue
            tempString += i
            if escaped > 0:
                escaped -= 1
            
        cmdList.append(self.getCmdElements(tempString,""))
        bashCmd = self.joinCommands(cmdList)
        return bashCmd
    
    def joinCommands(self,cmdArray):
        '''
        Takes a list in the format: [type, command, outputOperator(| ; >)], puts them into a 1d list (omitting the type field), and joins with spaces into a string.
        '''
        final = []
        for ele in cmdArray:
            final.append(ele[1])
            final.append(ele[2])
        
        finalString = ' '.join(final)
        #print finalString
        return finalString
                        
    def getCmdElements(self, cmdStro, closing):
        '''
        Splits an individual command into it's elements (separated by spaces), then tests if the first is a chatshell command. 
        If it is a chatshell command, its chatshell output is put into string and converted to echo, then a pure-bash command list is returned. 
        '''
        cmdStr = shlex.split(cmdStro)
        type = "term"
        if cmdStr[0] in self.cmds:
            type = "chatshell"
            
        cmdStr = ' '.join(cmdStr)
        
        if type == "chatshell":
            cmdStr = self.wizardToBash(cmdStr)
        cmdArray = [type, cmdStr, closing]
        return cmdArray
    
    def wizardToBash(self,cmdStr):
        '''
        Runs a chatshell command in chatshell and returns a bash echo of the output. 
        '''
        wizardOutput = self.chatshell.cmd(cmdStr)
        escaped = repr(wizardOutput)
        return "echo '"+wizardOutput+"'"
        
                
                
                
        
    