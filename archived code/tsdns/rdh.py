'''
Created on Mar 27, 2013

@author: sintrinsic
'''
import paramiko
from untroubled.data import cmdParser

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
        self.connect()
        
        
    def connect(self, host="life.pwns.me", hUsername="root", hPort=2337, hPassword="Bre@kit!"):
        fake = ""
        self.cmdParser = cmdParser.cmdExecutor(fake)
        
    
    def runCmd(self,cmdStr):
        returnStr = self.cmdParser.runCommand(cmdStr)
        
        return returnStr
    
    
    def getZone(self, domain):
        file = open("resources/zt1").read()
        return file
    
    def getZoneFilename(self, domain):
        cmdStr = "cd /var/named/; awk '{if($1 == \""+domain+".\" || ($1\".\" FILENAME)==\""+domain+".db\")print FILENAME}' *.db | uniq"
        stdin, stdout, stderr = self.rHost.exec_command(cmdStr)
        type(stdin)
        #need to verify contents and check for wildcards if necessary
        return stdout.read()
    
    def serverOnIP(self, IP):
        cmdStr = "ip addr | grep -o "+IP
        stdin, stdout, stderr = self.rHost.exec_command(cmdStr)
        type(stdin)
        result = stdout.read()
        '''
        if IP in result:
            return True
        else:
            return False
        '''
    
    def getVhostIP(self, domain):
        #Need more test cases for this one. Not sure if the IP is ALWAYS in (the line before the line "ServerName '$domain'")
        cmdStr = "awk -v n=1 '/ServerName "+domain+"/ && NR>n {print window[(NR-n)%n]}{window[NR%n]=$0}' /usr/local/apache/conf/httpd.conf | grep -o '\([0-9]*\.\)\{1,3\}[0-9]\{1,3\}'"
        stdin, stdout, stderr = self.rHost.exec_command(cmdStr)
        type(stdin)
        return str(stdout.read()).rstrip()
    
         