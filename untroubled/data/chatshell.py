'''
Created on Apr 7, 2013

@author: bdupree
'''
from paramiko import SSHClient, AutoAddPolicy
from time import sleep


class chatshell(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        
        self.__connection = SSHClient()
        self.__connection.set_missing_host_key_policy(AutoAddPolicy())
        self.__connection.connect("wizard2", username="bdupree", password="Bgd938784", look_for_keys=True)
        self.shell = self.__connection.invoke_shell()
        self.cmd("clear")
        '''
    
    def cmd(self, cmdStr):   
        '''
        while not self.shell.send_ready():
            sleep(.5)
        self.shell.sendall(cmdStr+"\n")
        while not self.shell.recv_ready():

            sleep(.01)
        self.shell.recv(2000000)
        respStr = ""
        keepAlive = True
        while keepAlive:
            while not self.shell.recv_ready():
                sleep(.1)
            resp = self.shell.recv(2000000)
            respStr = respStr + resp
            if "gsh-3.0 $" in respStr:
                keepAlive = False
        return respStr.replace("[24;1Hgsh-3.0 $ [J[24;11H", "")
        '''
        return ""
        
    def kill(self):
        self.shell.close()
        self.__connection.close()