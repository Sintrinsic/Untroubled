'''
Created on Sep 29, 2013

@author: bdupree
'''
import re, os, shlex, json, subprocess
import commands


class cmdExecutor(object):
    '''
    classdocs
    '''


    def __init__(self,chatShell):
        '''
        Constructor
        '''
        self.breakers = ["|",";",">"]
        cmdstr = open('/home/bdupree/git/Untroubled/untroubled/remoteCommands/commandList').read()
        self.cmds = cmdstr.split("\n")
        self.chatshell = chatShell
        
    def runCommand(self, cmdStr):
        bashCommand = self.parseCommands(cmdStr)
        cmdArray = shlex.split(bashCommand)
        output = commands.getoutput(bashCommand)
        
        #print "final output: "+output
        return output
    
        
    def parseCommands(self, cmdStr):
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
        final = []
        for ele in cmdArray:
            final.append(ele[1])
            final.append(ele[2])
        
        finalString = ' '.join(final)
        #print finalString
        return finalString
                        
    def getCmdElements(self, cmdStr, closing):
        cmdStr = shlex.split(cmdStr)
        type = "term"
        if cmdStr[0] in self.cmds:
            type = "chatshell"
            
        cmdStr = ' '.join(cmdStr)
        
        if type == "chatshell":
            cmdStr = self.wizardToBash(cmdStr)
        cmdArray = [type, cmdStr, closing]
        return cmdArray
    
    def wizardToBash(self,cmdStr):
        wizardOutput = self.chatshell.cmd(cmdStr)
        escaped = repr(wizardOutput)
        return "echo '"+wizardOutput+"'"
        
                
                
                
        
    