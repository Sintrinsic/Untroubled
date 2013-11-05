'''
Created on Nov 5, 2013

@author: bdupree
'''
from paramiko import SSHClient, AutoAddPolicy
from time import sleep
class ShellPool(object):


    def __init__(self):
        self.pool = []
        
        
class shell(object):
    
    def __init(self):
        self.loginCreds = open("../login").read().split(" ")
        self.__connection = SSHClient()
        self.__connection.set_missing_host_key_policy(AutoAddPolicy())
        self.__connection.connect("wizard2", username=self.loginCreds[0], password=self.loginCreds[1], look_for_keys=True)
        self.shell = self.__connection.invoke_shell()
        self.shell.combine_stderr = True
        self.shell.setblocking(1)