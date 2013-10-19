'''
Created on Oct 18, 2013

@author: sintrinsic
'''
from untroubled.dns.vZoneLocal import vZoneLocal
from untroubled.dns.vZoneRemote import vZoneRemote


class dnsManager(object):
    '''
    classdocs
    '''


    def __init__(self, domain, cmdExecutor):
        self.cmdExecutor = cmdExecutor
        self.remoteZone = vZoneRemote(domain, cmdExecutor)
        self.localZone = vZoneLocal(domain, cmdExecutor)
    