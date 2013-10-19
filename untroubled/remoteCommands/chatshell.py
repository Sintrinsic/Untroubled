'''
Created on Apr 7, 2013

@author: bdupree
'''
from paramiko import SSHClient, AutoAddPolicy
from time import sleep
from ftfy import fix_text

class chatshell(object):
    def __init__(self):
        self.loginCreds = open("../login").read().split(" ")
        self.__connection = SSHClient()
        self.__connection.set_missing_host_key_policy(AutoAddPolicy())
        self.__connection.connect("wizard2", username=self.loginCreds[0], password=self.loginCreds[1], look_for_keys=True)
        self.shell = self.__connection.invoke_shell()
        self.shell.combine_stderr = True
        self.shell.setblocking(1)
        self.timeout = .5
        self.prompt = self.getPrompt()
        
    def cmd(self, cmdStr):   
        if self.shell.recv_ready():
            print " ---- Warning: extra chars in buffer before chatshell.cmd start."
            self.shell.recv(2000000)
        while not self.shell.send_ready():
            sleep(.5)
        self.shell.sendall(cmdStr+"\n")
        while not self.shell.recv_ready():
            sleep(.01)
        resp = ""
        done = False
        waitTime = 0
        while not done:
            while not self.shell.recv_ready():
                if waitTime > self.timeout:
                    done = True
                    break
                sleep(.5)
                waitTime += .5
            if not done:
                resp += self.shell.recv(2000000)
            if self.prompt in resp:
                done = True      
        return fix_text(unicode(resp.strip(self.prompt).strip(cmdStr)))
        
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
        