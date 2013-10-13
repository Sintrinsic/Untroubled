'''
Created on Mar 9, 2013
need to find hostname of NS IP, and see if it matches
@author: sintrinsic
'''
import re
import numpy
import socket

class vZone(object):
    '''
    Virtual Zone parser that accepts a full text printout from either 'dig +trace domain' or cat '/var/named/domain.db'
    All that's needed is passing the full response of one of those commands as the 'records' arg.
    Nameservers according to this vZone stored in self.ns
    Final destination IP/domain stored in self.destination
    self.keyrecords contains all records that pertain to the resolution of this domain specifically
    self.errors contains troubleshooting issues that may need to be resolved for the domain to function properly.
    self.printInfo shows key records, errors found, and the final destination according to this vZone, for human-readable error-checking.
    Improvements needed:
        Only tested on a handful of domains. More testing is needed to see if other domains deviate from these patterns. 
    '''
    
    def __init__(self, records, domain, rHandler):
        '''
        Constructor
        '''
        self.remoteHandler = rHandler
        self.domain = domain
        self.exists = False
        self.type = "Unknown"
        self.soa = ""
        self.ns = [] #label,A record for NS (if exists)
        self.destination = [] #final result A or CNAME record
        self.keyRecords = []
        self.errors = []
        ''' records will be in format: [location_type=[[name,type,ttl,val],...],...] '''
        self.rawRecords = self.parseText(records);
        if self.type == "Dig":
            self.decodeDig(self.rawRecords)
        if self.type == "Zonefile":
            self.decodeZonefile(self.rawRecords)
        self.ns = numpy.asarray(self.ns)
        self.ns.sort(0)

    def parseText(self, text):
        text=text+"\n"
        nsName = re.compile(r'(?:^; Zone file for ).*?(?:\n)',re.MULTILINE)
        zoneFile = nsName.findall(text)
        if len(zoneFile)>0:
            self.zoneFile = re.sub("; Zone file for ","",str(zoneFile[0])).rstrip()
        '''dns record = ^[a-zA-z0-9\.]*.?\s+[0-9]*\s*IN\s+(NS|A|CNAME|SOA)\s+[a-zA-Z0-9\.\-]+   '''
        '''dig chunk = (^[a-zA-z0-9\.]+.?\s+[0-9]+?\s+?IN\s+?(NS|A|CNAME|SOA)\s+?[a-zA-Z0-9\.\-\s]+\n)+;;.*?\n  '''
        digExp = re.compile(r'((^([a-zA-z0-9\.\@]*)\s+([0-9]*)\s*IN\s+(NS|A|CNAME|SOA)\s+([a-zA-Z0-9\.\-]+)\n)+;;.*?\n)',re.MULTILINE)
        digMatches = digExp.findall(text)
        recExp = re.compile(r'^([a-zA-z0-9\.\@]*)\s+([0-9]*)\s*IN\s+(NS|A|CNAME|SOA)\s+([a-zA-Z0-9\.\-]+)',re.MULTILINE)
        
        #need to add check for if TLD doesn't exist.
        if len(digMatches) > 2:
            self.type = "Dig"
            chunks = []
            for row in numpy.asarray(digMatches)[2:,0]:
                chunks.append(recExp.findall(row))
        else:
            chunks = recExp.findall(text)
            self.type = "Zonefile"
        
        return chunks
 
    def decodeDig(self, records):
        records = numpy.asarray(records)
        domain = ""
        nsPing=False
        #registrar checks:
        if len(records)>0:
            self.exists = True
            regRecords = numpy.asarray(records[0])
            if len(regRecords)>0:
                nsRecords = regRecords[regRecords[0:,2]=="NS"]
                for ns in nsRecords:
                    domain = ns[0]
                    nsType = "external"
                    nsIP = "NO IP."
                    if ns[0] in ns[3]:
                        nsType = "self-registered"
                    try:
                        nsIP = socket.gethostbyname(ns[3])
                        nsPing = True
                    except:
                        self.errors.append(ns[3]+" is not registered to an IP.")
                    self.ns.append([ns[3], nsType, nsIP])
                    ns = numpy.append(ns, nsIP)
                    self.keyRecords.append(ns)
            else:
                self.errors.append("This domain is registered but has no nameservers set.")
                return
            
            
        else: 
            self.errors.append("This domain isn't registered.")
            return
        if len(records)>1:
            authRecords = numpy.asarray(records[1])
            selfRecords = authRecords[(authRecords[0:,2]=="CNAME") | (authRecords[0:,2]=="A")]
            selfRecords = selfRecords[(selfRecords[0:,0]== self.domain+".")]
            if len(selfRecords)>0:
                self.destination = selfRecords[0,3]
                #self.keyRecords.append(selfRecords[0])
                for record in selfRecords:
                    self.keyRecords.append(record)
            else:
                self.errors.append("No A/CNAME record returned.")

        else:
            if nsPing:
                self.errors.append("No authoritative zone provided at these nameservers.")

            
    def decodeZonefile(self, records):
        if len(records)<1:
            self.destination = ""
            self.errors.append("This domain isn't set up on the target server.")
            return
        self.exists = True
        records = numpy.asarray(records)
        #Create arrays for the key record types (can be empty)
        soaRecord = records[records[0:,2]=="SOA"]
        nsRecords = records[records[0:,2]=="NS"]
        
        #Set vZone SOA property.
        if len(soaRecord)>0:
            self.soa = soaRecord[0,3]
            self.keyRecords.append(soaRecord[0])
        else:
            self.errors.append("This Zone File has no SOA record")
        
        #set vZone NS property .
        if len(nsRecords)>0:
            for ns in nsRecords:
                self.keyRecords.append(ns)
                if ns[0] in ns[3]: #do private nameserver checks
                    nsSub = re.sub('.'+ns[0], '', ns[3]) #strip the domain from the NS subdomain to get the value of the A record. 
                    nsArecord = records[records[0:,0]==(nsSub or ns[3])]
                    if len(nsArecord)==1:#Checks if an A record exists for this self-private NS entry. 
                        self.ns.append([ns[3], "A Record", nsArecord[0,3]])
                    else:
                        aRecordZone = self.remoteHandler.getZone(ns[3][:-1])
                        if len(aRecordZone)>1: #Checks to see if the NS in question exists an ANY zone on the server
                            self.ns.append(ns[3], "Separate A record", )
                        else:    
                            self.errors.append(ns[3]+"is a private nameserver of "+ns[0]+" but does not have a corresponding A record or independent local Zonefile")
                else:
                    self.ns.append([ns[3], "External Record", None])

        #define target domain records (A or CNAME roecords that refer specifiallcy to the domain this script is searching for)
        targetDomain = re.sub(self.zoneFile,"",self.domain)[:-1]
        ACRecords = records[(records[0:,2]=="CNAME") | (records[0:,2]=="A")]
        if len(targetDomain)>0:
            targetRecords = ACRecords[(ACRecords[0:,0]== targetDomain)]
        zoneDomainRecords = ACRecords[(ACRecords[0:,0]== self.zoneFile+".")]
        

        #Error checks
        if len(self.soa) > 1:
            if soaRecord[0,3] not in nsRecords:
                self.errors.append(soaRecord[0,3]+"is the SOA nameserver, but that nameserver isn't a nameserver in this zone.")
        else:
            self.errors.append("This zone has no SOA record.")
            
        if len(self.ns) <2:
            self.errors.append("This zone has less than the required 2 nameserver entries in the glue.")
        
        if len(zoneDomainRecords)==1:
            self.destination = zoneDomainRecords[0,3]
        else:
            if len(zoneDomainRecords)>1:
                self.errors.append("There is more than one root A/CNAME record for this domain.")
            else:
                self.errors.append("There is not a root A/CNAME record for this domain.")
        for zdRecord in zoneDomainRecords:
            self.keyRecords.append(zdRecord)
            
        if len(targetDomain) > 0: #only do the following if the target domain is different than the base domain for this zonefile
            if len(targetRecords)==1:
                self.destination = targetRecords[0,3] #overwrites destination if the domain arg is different from the zonefile's base domain. 
            else:
                if len(targetRecords)>1:
                    self.errors.append("There is more than one root A/CNAME record for the target subdomain.")
                else:
                    self.errors.append("There is not a root A/CNAME record for the target subdomain.")
            for tRecord in targetRecords:
                self.keyRecords.append(tRecord)        

    def printInfo(self):
        errors = []
        if not self.exists:
            errors.append("Not found.")
            return
        info = "Key records:\n"
        for record in self.keyRecords:
            recordStr = record[0]+"\t"+record[1]+"\tIN\t"+record[2]+"\t"+record[3]
            if len(record) > 4:
                recordStr = recordStr+" ("+record[4]+")"
            info += recordStr+"\n"
        errors.append(info)
        info = "Final destination for domain/subdomain:\n"+str(self.destination)+"\n"
        errors.append(info)
        info = "Errors:\n"
        if len(self.errors)>0:
            for error in self.errors:
                info += error+"\n"
        else:
            info += "None Found"
        errors.append(info)
        return errors
        
            
    