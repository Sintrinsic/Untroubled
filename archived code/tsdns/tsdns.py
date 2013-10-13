'''
Created on Mar 9, 2013

@author: sintrinsic
'''
from vzone import vZone
import numpy
import subprocess
import shlex
import sys
from rdh import rdh

class tsdns(object):
    def __init__(self,domain,server):
        self.errors = []
        '''
        To do:
        1.Args need to be [domain, server] and error checked, returning help/syntax on errors.
        2.Need a class (or alteration of rdh) to fetch a hg server by name and provide login credentials, or a way to connect via key if appropriate. 
        3.Need a concusion check to inform you if the remote NS records DO point to a HG server, but not the one you've checked on, and provide that server name. 
        4.Get more test cases.
        5.Clean things up. 
        '''
        domainArg = domain
        
        remoteHandler = rdh()
        serverZoneText = remoteHandler.getZone(domainArg)
        errors = {"External":[],"Local":[],"Conclusion":[]}
        cmdStr = 'dig +trace '+domainArg
        cmd = subprocess.Popen(shlex.split(cmdStr), stdout=subprocess.PIPE)
        digRespText,err=cmd.communicate()
        digZone = vZone(digRespText, domainArg, remoteHandler)   
        serverZone = vZone(serverZoneText, domainArg, remoteHandler)
        #digZone.printInfo() 
        
        errors["External"].extend(digZone.printInfo()) 
        errors["Local"].extend(serverZone.printInfo())
        #Temp checks unti I have time for something more concrete
        if (len(digZone.destination)>0) and remoteHandler.serverOnIP(digZone.destination):
            errors["Conclusion"].append("The remote records are pointing to an IP on this server ("+digZone.destination+").")
            if(len(digZone.ns)>0 and len(serverZone.ns) > 0 and numpy.all(digZone.ns[0:,0] == serverZone.ns[0:,0])):
                errors["Conclusion"].append("The Local nameservers match those at the registrar.")
            else:
                if serverZone.exists:
                    errors["Conclusion"].append("The Local nameservers do NOT match those at the registrar.")
        else:
            badNSips = digZone.ns[0:,2]=="NO IP."
            goodNSips = digZone.ns[0:,2]!="NO IP."
            if (not numpy.all(badNSips)) and remoteHandler.serverOnIP(digZone.ns[goodNSips][0,2]) :
                errors["Conclusion"].append("The remote nameservers for the base domain point to this server.")
            else:
                errors["Conclusion"].append("The remote records for this domain do NOT point to this server.")
        
        if not serverZone.exists:
            errors["Conclusion"].append("No zonefile exists for this domain/subdomain on the target server.")
            
    
    
        vhostIP = remoteHandler.getVhostIP(domainArg)
        if len(vhostIP)>1 and serverZone.exists:
            if vhostIP != serverZone.destination:
                errors["Conclusion"].append("The IP the server's zonefile points to is "+digZone.destination+" but the vhosts entry says it should be "+vhostIP+".")
            else:
                errors["Conclusion"].append("Zonefile IP matches vhost IP.")
        else:
            errors["Conclusion"].append("No vhost entry found for this domain.")
        remoteHandler.rHost.close()
        self.errors = errors