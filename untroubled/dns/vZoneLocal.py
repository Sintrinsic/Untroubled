import re

class vZoneLocal(object):
    '''
    Loads a raw DNS zonefile and parses out the records vital to the target domain. 
    Does analysis on conflicting, incorrect, and missing records.
    Acquires vital information on IPs and domains such as the IP of external domain references and the hostname of any IP listed.
    Compiles known errors in its errors list.
    Provides interface members to fetch, display, and compare records (with other vZone files)
    To-do: LOTS
    '''
    
    def __init__(self, domain, commandExecutor, server = None):

        self.patternDomain = re.compile(r'([\b\s^]+)?(([a-zA-Z\d\-]+\.)+([A-Za-z\-]+))(\.)?')

        self.commandExecutor = commandExecutor
        self.domain = domain

        self.keyRecords = []    
        self.miscRecords = []
        self.destination = [] #final result A or CNAME record    
        self.typedRecords = {"@":[],"NS":[],"SOA":[],"MX":[],"Related":[]}
        
        self.errors = []
        
        self.text = self.commandExecutor("./viewzone "+domain)
        self.rawRecords = self.parseText(self.text)
        self.decode(self.rawRecords)
        self.printRecords()
        
        self.server = None
        self.vHostIP = None
        self.exists = False        

        
    def parseText(self, text):
        #^([a-zA-z0-9\.\@]*)\s+([0-9]*)\s*IN\s+([A-Z]{1,9})\s+([a-zA-Z0-9\.\-]+)
        #recExp = re.compile(r'(?:([\w\.\d\@]+)[\t\s!\n]+([\d]+[\s\t])?IN\s+([\w]+)\s+([\d\w\.\"\= \+\:\?\;\/\\\-]+(?:[\r\n])))+',re.MULTILINE)
        recExp = re.compile(r'^([\w\.\d\@]+)[\s!\n]+([\d]+)?(?:\s)?IN\s+(A|NS|SOA|CNAME)\s+([\d\w\.\"\= \+\:\?\;\/\\\-]+)',re.MULTILINE)
        #need to add check for if TLD doesn't exist.
        
        chunks = recExp.findall(text)
        nsName = re.compile(r'(?:^; Zone file for ).*?(?:\n)',re.MULTILINE)
        zoneFile = nsName.findall(text)
        if len(zoneFile)>0:
            self.text = re.sub("; Zone file for ","",str(text[0])).rstrip()
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
        if rootDomain in self.text:
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
        
        
    #Generates a regex string that matches all possible variants that the target domain could be labeled as (example: mail or mail.domain.com)
    def getSubPatternString(self,domain):
        subDomain = re.sub(self.text,"",domain)[:-1]
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
        
        
    def getResolvingIP(self,domain):
        digOutput = self.commandExecutor.runCommand("dig +short A "+domain)
        if digOutput:
            return digOutput
        else:
            return "Offline" 

    
    def getVhostIP(self):
        '''
        ToDo:
        uf = self.commandExecutor("uf "+self.domain+" "+self.server)
        vHostIP = (parse ip from UF output)
        return vHostIP
        '''
        return "192.168.0.1"
    
    
    def getServer(self, ip):
        '''
        ToDo: 
        ipid = self.commandExecutor.runCommand("ipid "+ip)
        server = (parse server name from output)
        return server 
        '''
        return "gator1234.hostgator.com"
        
