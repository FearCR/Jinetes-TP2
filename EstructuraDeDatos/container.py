
class Node:
#Inicializador, hay que agregar una variable para cada parte
    def __init__(self):
        self.id=""
        self.threats= Threats()
        self.vulnerabilities= Vulnerabilities()
#Metodos set de nodos, aqui hay que agregar un set para cada parte
    def setId(self, id):
        self.id = id
    def setThreats(self, threats):
        self.threats = threats
    def setVulnerabilities(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities
#Print all, hay que agregar un print para cada parte para probarla
    def printAll(self):
        print("IMPRESION DE NODO")
        print("ID NODO= "+self.id)
        print("LISTA DE THREATS:")
        self.threats.printThreats()
        print("LISTA DE VULNERABILITIES:")
        self.vulnerabilities.printVulnerabilities()

#Clase de Lista de threats
class Threats:
#Inicializador
    def __init__(self):
        self.threatList=[]
#Agrega una nueva Threat a la lista
    def addThreat(self,threat):
        self.threatList.append(threat)
#Impresion
    def printThreats(self):
        for threat in self.threatList:
            threat.printThreat()

#Clase Threat
class Threat:
#Inicializador, una variable por cada valor para captar
    def __init__(self):
        self.id=""
        self.name=""
        self.description=""
        self.vulnerability=""
#Metodo para probar set de todos los valores no hace falta
    def setAll(self,newID,newName,newDescription,newVulnerability):
        self.id=newID
        self.name=newName
        self.description=newDescription
        self.vulnerability=newVulnerability
#Metodos set para Threat, uno por valor por captar
    def setId(self,newID):
        self.id=newID

    def setName(self,newName):
        self.name=newName

    def setDescription(self,newDescription):
        self.description=newDescription

    def setVulnerability(self,newVulnerability):
        self.vulnerability=newVulnerability
#Print
    def printThreat(self):
        print(self.id,self.name, self.description,self.vulnerability)
#Clase de Lista de threats
class Vulnerabilities:
#Inicializador
    def __init__(self):
        self.vulnerabilityList=[]
#Agrega una nueva Threat a la lista
    def addVulnerability(self,vulnerability):
        self.vulnerabilityList.append(vulnerability)
#Impresion
    def printVulnerabilities(self):
        for vulnerability in self.vulnerabilityList:
            vulnerability.printVulnerability()
#Clase Vulnerability
class Vulnerability:
#Inicializador, una variable por cada valor para captar
    def __init__(self):
        self.id=""
        self.sourceDB=""
        self.name=""
        self.referenceSecurity=""
        self.overview=""
        self.description=""
        self.impact=""
        self.severity=""
#Metodo para probar set de todos los valores no hace falta
    def setAll(self,newID,newDB,newName,newReferenceSecurity,newOverview,newDescription,newImpact,newSeverity):
        self.id=newID
        self.sourceDB=newDB
        self.name=newName
        self.referenceSecurity=newReferenceSecurity
        self.overview=newOverview
        self.description=newDescription
        self.impact=newImpact
        self.severity=newSeverity
#Metodos set para Threat, uno por valor por captar
    def setId(self,newID):
        self.id=newID

    def setSourceDB(self,newDB):
        self.sourceDB=newDB

    def setName(self,newName):
        self.name=newName

    def setReferenceSecurity(self,newReferenceSecurity):
        self.referenceSecurity=newReferenceSecurity

    def setOverview(self,newOverview):
        self.overview=newOverview

    def setDescription(self,newDescription):
        self.description=newDescription

    def setImpact(self,newImpact):
        self.impact=newImpact

    def setSeverity(self,newSeverity):
        self.severity=newSeverity
#Print
    def printVulnerability(self):
        print(self.id,self.sourceDB,self.name,self.referenceSecurity,self.overview,self.description,self.impact,self.severity)
