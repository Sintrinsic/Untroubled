'''
Created on Mar 9, 2013
need to find hostname of NS IP, and see if it matches
@author: sintrinsic
'''
import re
import numpy
import socket

class vZoneLocal(object):
    '''
    Virtual Zone parser that accepts a full text printout from either 'dig +trace domain' or cat '/var/named/domain.db'
    All that's needed is passing the full response of one of those commands as the 'records' arg.
    Nameservers according to this vZoneLocal stored in self.ns
    Final destination IP/domain stored in self.destination
    self.keyrecords contains all records that pertain to the resolution of this domain specifically
    self.errors contains troubleshooting issues that may need to be resolved for the domain to function properly.
    self.printInfo shows key records, errors found, and the final destination according to this vZoneLocal, for human-readable error-checking.
    Improvements needed:
        Only tested on a handful of domains. More testing is needed to see if other domains deviate from these patterns. 
    '''
    
    def __init__(self, records, domain, rdh):
        '''
        Constructor
        '''
        self.patternDomain = re.compile(r'([\b\s^]+)?(([a-zA-Z\d\-]+\.)+([A-Za-z\-]+))(\.)?')

        self.remoteHandler = rdh
        self.domain = domain
        self.server = "gator1234.hostgator.com"
        self.vHostIP = self.getVhostIP()
        self.exists = False
        self.keyRecords = []    
        self.miscRecords = []
        self.destination = [] #final result A or CNAME record    
        self.errors = []
        self.typedRecords = {"@":[],"NS":[],"SOA":[],"MX":[],"Related":[]}
        self.zoneFile = ""
        records = open("/home/bdupree/workspace/Untroubled/untroubled/dns/zt1").read()
        self.rawRecords = self.parseText(records);
        self.decode(self.rawRecords)
        self.printRecords()
        

        
    def parseText(self, text):
        #^([a-zA-z0-9\.\@]*)\s+([0-9]*)\s*IN\s+([A-Z]{1,9})\s+([a-zA-Z0-9\.\-]+)
        #recExp = re.compile(r'(?:([\w\.\d\@]+)[\t\s!\n]+([\d]+[\s\t])?IN\s+([\w]+)\s+([\d\w\.\"\= \+\:\?\;\/\\\-]+(?:[\r\n])))+',re.MULTILINE)
        recExp = re.compile(r'^([\w\.\d\@]+)[\s!\n]+([\d]+)?(?:\s)?IN\s+(A|NS|SOA|CNAME)\s+([\d\w\.\"\= \+\:\?\;\/\\\-]+)',re.MULTILINE)
        #need to add check for if TLD doesn't exist.
        
        chunks = recExp.findall(text)
        nsName = re.compile(r'(?:^; Zone file for ).*?(?:\n)',re.MULTILINE)
        zoneFile = nsName.findall(text)
        if len(zoneFile)>0:
            self.zoneFile = re.sub("; Zone file for ","",str(zoneFile[0])).rstrip()
        return chunks
            
    def decode(self, records):
        if len(records)<1:
            self.destination = ""
            self.errors.append("This domain isn't set up on the target server.")
            return
        self.exists = True
        patternString = self.getSubPatternString(self.domain)
        mainRecordPattern = re.compile(patternString)
    
        # Gather Vital records
        for record in records:
            case = record[2]
            isMain = mainRecordPattern.match(record[0])
            record = list(record)
            record.extend(record.pop(3).split(" "))
            if isMain:
                if case=="A" or case =="CNAME" :
                    record[0] = self.cleanTrailingDot(record[0])
                    self.typedRecords["@"].append(record)
                    self.keyRecords.append(record)
                    continue
            if case=="SOA":
                self.typedRecords["SOA"].append([self.cleanTrailingDot(record[3])])
                self.keyRecords.append(record)
                continue
            if case=="NS":
                self.typedRecords["NS"].append([self.cleanTrailingDot(record[3])])
                self.keyRecords.append(record)
                continue
            if case=="MX":
                self.typedRecords["MX"].append([self.cleanTrailingDot(e) for e in record[3:5]])
                continue
            self.miscRecords.append(record)
        
        # Verify single @ record
        for dest in self.typedRecords["@"]:
            self.destination.append(dest[3])

            
    def findErrors(self):
        if len(self.destination) > 1:
            errorStr = "More than one @ record in zonefile."
        elif len(self.destination)<1:
            errorStr = "No @ record in zonefile."
        self.errors.append(errorStr)
        if self.typedRecords["SOA"][0] not in self.typedRecords["NS"]:
            self.errors.append("SOA record doesn't match an NS record.")
        
        
            
        
    #Check first if the target domain is in the same zonefile. If it is, get the IP from here and add the corresponding record to keyrecords and return IP. Else, get remote IP and return.
    def getDomainIP(self,domain):
        targetDomain = re.sub("[\s\.]+$","", domain)
        rootDomain = ".".join(targetDomain.split(".")[-1:])
        ip = " "
        if rootDomain in self.zoneFile:
            subPattern = re.compile(self.getSubPatternString(targetDomain))
            for r in self.rawRecords:
                if subPattern.match(r[0]) and (r[2] == "A" or r[2] == "CNAME"):
                    if r not in self.keyRecords:
                        self.typedRecords["Related"].append(r)
                        self.keyRecords.append(r)
                    ip += r[3]+" "
        else:
            ip = " "+self.ping(targetDomain)+" "
        return ip
        
    #Generates a regex tring that matches all possible variants that the target domain could be labled as (example: mail or mail.domain.com)
    def getSubPatternString(self,domain):
        subDomain = re.sub(self.zoneFile,"",domain)[:-1]
        return '^('+self.domain+('|'+subDomain if subDomain else '')+')(\.)?'
    
    def printRecords(self):
        records = ""
        records += self.recordsToString("@", self.typedRecords["@"])+"\n"
        records += self.recordsToString("NS", self.typedRecords["NS"])+"\n"
        records += self.recordsToString("SOA", self.typedRecords["SOA"])+"\n"
        records += self.recordsToString("MX", self.typedRecords["MX"])+"\n"
        if len(self.typedRecords["Related"])>0:
            records += self.recordsToString("Related", self.typedRecords["Related"])+"\n"
        return records

    
    def recordsToString(self,title, records):
        returnString = title+":\n"
        for record in records:
            returnString += '  '+' '.join(record)+"\n" 
        return returnString
    
    def cleanTrailingDot(self,domain):
        elements = self.patternDomain.findall(domain)
        if elements: 
            domain = elements[0][1]
        return domain
        
    def ping(self,domain):
        return "192.168.0.1"
    
    def getVhostIP(self):
        return "192.168.0.1"
    
    def getServer(self, ip):
        return "gator1234.hostgator.com"
        
