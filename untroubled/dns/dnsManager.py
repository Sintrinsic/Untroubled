'''
Created on Oct 18, 2013

@author: sintrinsic
'''
from untroubled.dns.vZoneLocal import vZoneLocal
from untroubled.dns.vZoneRemote import vZoneRemote
import re

class dnsManager(object):
    '''
    classdocs
    '''
    def __init__(self, domain, cmdExecutor):
        self.cmdExecutor = cmdExecutor
        hgid = self.cmdExecutor.runCommand('ui ushli.org | grep Server: | cut -d": " -f2')
        server = ""
        if len(hgid)>3:
            server = hgid
        print "DNS troubleshooter: targetserver: "+server
        
        self.remoteZone = vZoneRemote(domain, cmdExecutor)
        self.localZone = vZoneLocal(domain, cmdExecutor, server)
    