
import re, numpy, socket
from rdh import rdh

class vZoneRemote(object):
    '''
    Runs a dig +trace $targetDomain and parses out the records vital to the target domain on both the registrar and authoritative level. 
    Does analysis on delegation path, including the validity of the nameservers at the registrar, and the congruity/accessibility of the authoritative zone. 
    Acquires vital information on IPs and domains such as the IP of domain references and the hostname of any IP listed.
    Compiles known errors in its errors list.
    Provides interface members to fetch, display, and compare records (with other vZone files)
    To-do: LOTS
    '''
    
    def __init__(self, domain):
        self.patternDomain = re.compile(r'([\b\s^]+)?(([a-zA-Z\d\-]+\.)+([A-Za-z\-]+))(\.)?')

        self.remoteHandler = rdh()
        self.domain = domain
        self.server = "gator1234.hostgator.com"
        self.vHostIP = self.getVhostIP()
        self.exists = False
        self.keyRecords = []    
        self.miscRecords = []
        self.destination = [] #final result A or CNAME record    
        self.errors = []
        self.registrar = []
        self.auth = []
        self.typedRecords = {"Registrar":[],"Authoritative":[]}
        self.zoneFile = ""
        records = self.getTrace(domain)
        self.rawRecords = self.parseText(records);
        self.decode(self.rawRecords)

        
    def getTrace(self,domain):
        return self.remoteHandler.dig(domain)
        
    def parseText(self, text):
        text=text+"\n\n"

        '''dns record = ^[a-zA-z0-9\.]*.?\s+[0-9]*\s*IN\s+(NS|A|CNAME|SOA)\s+[a-zA-Z0-9\.\-]+   '''
        '''dig chunk = (^[a-zA-z0-9\.]+.?\s+[0-9]+?\s+?IN\s+?(NS|A|CNAME|SOA)\s+?[a-zA-Z0-9\.\-\s]+\n)+;;.*?\n  '''
        digExp = re.compile(r'(.+?)(?:;;.+?ms)',re.S)
        digMatches = digExp.findall(text)
        recExp = re.compile(r'^([\w\.\d\@]+)[\s!\n]+([\d]+)?(?:\s)?IN\s+(A|NS|SOA|CNAME)\s+([\d\w\.\"\= \+\:\?\;\/\\\-]+)',re.MULTILINE)
        
        #need to add check for if TLD doesn't exist.
        if len(digMatches) > 2:
            chunks = []
            for row in digMatches:
                recs = recExp.findall(row)
                chunks.append(recs)
        else:
            return ["Domain doesn't exist"]
        
        return chunks
            
    def decode(self, records):
        self.exists = True
        patternString = self.getSubPatternString(self.domain)
        mainRecordPattern = re.compile(patternString)
        for record in records[2]:
            self.typedRecords["Registrar"].append(record)
        for record in records[3]:
            self.typedRecords["Authoritative"].append(record)


            
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
        records += self.recordsToString("Registrar", self.typedRecords["Registrar"])+"\n"
        records += self.recordsToString("Authoritative", self.typedRecords["Authoritative"])+"\n"

        return records

    
    def recordsToString(self,title, records):
        returnString = title+":\n"
        for record in records:
            record = list(record)
            del record[1]
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
    
    
vz = vZoneRemote("life.pwns.me")

    
        