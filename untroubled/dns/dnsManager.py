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
        hgid = self.cmdExecutor.runCommand("hgid "+domain)
        infoPat = re.compile("\|([0-9a-zA-Z\.\- ]*)\|\s("+domain+")\s\|(.*)\|", re.MULTILINE)
        matches = infoPat.findall(hgid)
        server = ""
        if len(matches)>2:
            server = matches[0]
        print server
        
        self.remoteZone = vZoneRemote(domain, cmdExecutor)
        self.localZone = vZoneLocal(domain, cmdExecutor, server)
    