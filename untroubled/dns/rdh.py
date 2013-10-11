'''
Created on Mar 27, 2013

@author: sintrinsic
'''
from untroubled.data.cmdParser import cmdExecutor
class rdh(object):
    '''
    Remote Data Handler class:
    Used as an easily customizable interface to:
      1. Connect to a remote server
      2. Fetch the following:
          1. A zonefile at /var/named/domain.db
          2. Get the vhost IP for a given domain from /usr/local/apache/conf/httpd.conf
          3. Check if a given IP blongs to the server.  
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cmdExecutor = cmdExecutor(" ")
    
    def getZone(self, domain):
        pass
    
    def serverOnIP(self, IP):
        pass
    
    def dig(self, domain):
        return self.cmdExecutor.runCommand("dig +trace "+domain)
    
    def getVhostIP(self, domain):
        #Need more test cases for this one. Not sure if the IP is ALWAYS in (the line before the line "ServerName '$domain'")
        cmdStr = "awk -v n=1 '/ServerName "+domain+"/ && NR>n {print window[(NR-n)%n]}{window[NR%n]=$0}' /usr/local/apache/conf/httpd.conf | grep -o '\([0-9]*\.\)\{1,3\}[0-9]\{1,3\}'"
        stdin, stdout, stderr = self.rHost.exec_command(cmdStr)
        type(stdin)
        return str(stdout.read()).rstrip()
    
         