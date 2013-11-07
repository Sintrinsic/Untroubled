'''
Created on Apr 7, 2013

@author: bdupree
'''
from paramiko import SSHClient, AutoAddPolicy
from time import sleep
from ftfy import fix_text
import re

class chatshell(object):
    activePool = []
    inactivePool = []
    shellCount = 0
    
    @staticmethod
    def __getChatShell():
        if len(chatshell.inactivePool) < 1:
            shell=trueChatshell()
            chatshell.shellCount += 1
            print "Chatshell count increased: "+str(chatshell.shellCount)
        else:
            print "Shell allocated"
            shell=chatshell.inactivePool.pop(0)
        chatshell.activePool.append(shell)
        return shell    
    
    @staticmethod
    def __returnChatShell(shell):
        if shell in chatshell.activePool:
            print "Shell returned"
            chatshell.activePool.pop(chatshell.activePool.index(shell))
            chatshell.inactivePool.append(shell)
        else:
            print "WARNING: Shell returned when not active"
            
            
    def cmd(self, cmdStr):
        shell = chatshell.__getChatShell()
        output = shell.cmd(cmdStr)
        chatshell.__returnChatShell(shell)
        return output
    
    
    
    
    


class trueChatshell(object):
    
    def __init__(self):
        self.loginCreds = open("../login").read().split(" ")
        self.__connection = SSHClient()
        self.__connection.set_missing_host_key_policy(AutoAddPolicy())
        self.__connection.connect("wizard2", username=self.loginCreds[0], password=self.loginCreds[1], look_for_keys=True)
        self.shell = self.__connection.invoke_shell()
        self.shell.combine_stderr = True
        self.shell.setblocking(1)
        self.timeout = 3
        self.prompt = fix_text(unicode(self.getPrompt()))
        self.promptPattern = re.compile("^"+re.escape(self.prompt)+"$", re.MULTILINE)
        
    def cmd(self, cmdStr):   
        if self.shell.recv_ready():
            print " ---- Warning: extra chars in buffer before chatshell.cmd start."
            self.shell.recv(2000000)
        while not self.shell.send_ready():
            sleep(.5)
        self.shell.sendall(cmdStr)
        cmdRespStr = ""
        cmdPatternStr= re.escape(cmdStr)
        cmdDonePattern = re.compile(cmdPatternStr)
        cmdDone = False
        while not cmdDone:
            while not self.shell.recv_ready():
                sleep(.1)
            cmdRespStr += self.shell.recv(20000)
            fixed = fix_text(unicode(cmdRespStr))
            found = cmdDonePattern.findall(fixed)
            if len(found) > 0:
                cmdDone = True
        self.shell.sendall("\n")

        resp = ""
        done = False
        waitTime = 0
        while not done:
            while not self.shell.recv_ready():
                if waitTime > self.timeout:
                    done = True
                    break
                sleep(.1)
                waitTime += .1
            if not done:
                resp += self.shell.recv(2000000)
            '''
            if self.prompt in fix_text(unicode(resp)):
                done = True
            '''
            found = self.promptPattern.findall(fix_text(unicode(resp)))
            if len(found) > 0:
                done = True     
        return fix_text(unicode(resp)).strip(self.prompt).strip(cmdStr)
        
    def getPrompt(self):
        resp = ""
        while not self.shell.recv_ready():
            sleep(.1)
        while self.shell.recv_ready():
            resp += self.shell.recv(2000000)
            waitTime = 0
            while not self.shell.recv_ready():
                waitTime += .1
                if waitTime > self.timeout:
                    break
                sleep(.1)
        respLines = resp.split("\n")
        return respLines[-1]
                
    def kill(self):
        self.shell.close()
        self.__connection.close()
