#------------------Clase NODO--------------------------
class Node:
#Inicializador, hay que agregar una variable para cada parte
    def __init__(self):
        self.id=""
        self.threats= Threats()
        self.vulnerabilities= Vulnerabilities()
        self.security_Controls= Security_Controls()
        self.basic_Information= Basic_Information()
        self.security_policies = security_policies()
        self.security_relationships = security_relationships()
#Metodos set de nodos, aqui hay que agregar un set para cada parte
    def setId(self, id):
        self.id = id
    def setThreats(self, threats):
        self.threats = threats
    def setSecurity_Policies(self, security_policies):
		self.security_policies = security_policies
    def setSecurity_Relationships(self, security_relationships):
		self.security_relationships = security_relationships
    def setVulnerabilities(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities
    def setSecurity_Controls(self, security_controls):
        self.security_Controls = security_controls
    def setBasic_Information(self, basic_information):
        self.basic_Information = basic_information
#Print all, hay que agregar un print para cada parte para probarla
    def printAll(self):
        print("IMPRESION DE NODO")
        print("ID NODO= "+self.id)
        print("LISTA DE BASIC INFORMATION:")
        self.basic_Information.printBasic_Information()
        print("LISTA DE THREATS:")
        self.threats.printThreats()
        print("LISTA DE VULNERABILITIES:")
        self.vulnerabilities.printVulnerabilities()
        print("LISTA DE SECURITY CONTROL:")
        self.security_Controls.printSecurity_Controls()
        print("LISTA DE SECURITY POLICIES:")
        self.security_policies.print_security_policies()
        print("LISTA DE SECURITY RELATIONSHIPS:")
        self.security_relationships.print_security_relationships()

#------------------Clase NODO-------------------------------------
#--------------------Clase de Lista de THREATS---------------------
class Threats:
#Inicializador
    def __init__(self):
        self.threatList=[]
#Agrega una nueva THREAT a la lista
    def addThreat(self,threat):
        self.threatList.append(threat)
#Impresion
    def printThreats(self):
        for threat in self.threatList:
            threat.printThreat()
#--------------------Clase de Lista de THREATS---------------------
#------------------------Clase THREAT----------------------------
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
#Metodos set para THREAT, uno por valor por captar
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
#------------------------Clase THREAT----------------------------

#---------------------Clase de Lista de VULNERABILITIES-------------------
class Vulnerabilities:
#Inicializador
    def __init__(self):
        self.vulnerabilityList=[]
#Agrega una nueva VULNERABILITY a la lista
    def addVulnerability(self,vulnerability):
        self.vulnerabilityList.append(vulnerability)
#Impresion
    def printVulnerabilities(self):
        for vulnerability in self.vulnerabilityList:
            vulnerability.printVulnerability()
#---------------------Clase de Lista de VULNERABILITIES-------------------
#---------------------------Clase VULNERABILITY----------------------------------
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
#Metodos set para VULNERABILITY, uno por valor por captar
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
#---------------------------Clase VULNERABILITY----------------------------------

#-----------------------Clase de Lista de SECURITY CONTROL-----------------------
class Security_Controls:
#Inicializador
    def __init__(self):
        self.security_ControlList=[]
#Agrega una nueva SECURITY CONTROL a la lista
    def addSecurity_Control(self,security_control):
        self.security_ControlList.append(security_control)
#Impresion
    def printSecurity_Controls(self):
        for security_control in self.security_ControlList:
            security_control.printSecurity_Control()
#-----------------------Clase de Lista de SECURITY CONTROL------------------

#-----------------------Clase SECURITY CONTROL-----------------------------
class Security_Control:
#Inicializador, una variable por cada valor para captar
    def __init__(self):
        self.id=""
        self.name=""
        self.description=""
        self.securityPolicyID=""
#Metodo para probar set de todos los valores no hace falta
    def setAll(self,newID,newName,newDescription,newSecurityPolicyID):
        self.id=newID
        self.name=newName
        self.description=newDescription
        self.securityPolicyID=newSecurityPolicyID
#Metodos set para SECURITY CONTROL, uno por valor por captar
    def setId(self,newID):
        self.id=newID

    def setName(self,newName):
        self.name=newName

    def setDescription(self,newDescription):
        self.description=newDescription

    def setSecurityPolicyID(self,newSecurityPolicyID):
        self.securityPolicyID=newSecurityPolicyID
#Print
    def printSecurity_Control(self):
        print(self.id,self.name,self.description,self.securityPolicyID)
#-----------------------Clase SECURITY CONTROL-----------------------------

#-----------------------Clase BASIC INFORMATION-----------------------------
class Basic_Information:
#Inicializador, una variable por cada valor para captar
    def __init__(self):
        self.name=""
        self.overview=""
        self.properties=[]


#Metodos set para BASIC INFORMATION, uno por valor por captarD
    def setName(self,newName):
        self.name=newName

    def setOverview(self,newOverview):
        self.overview=newOverview
    def setProperties(self,list):
        for x in range(len(list)):
            self.properties.append(list[x])


#Print
    def printBasic_Information(self):
        print(self.name,self.overview, self.properties)
#-----------------------Clase BASIC INFORMATION-----------------------------



class security_policies:
	def __init__(self):
		self.security_policies_list = []
	
	def add_security_policie(self, security_policie):
		self.security_policies_list.append(security_policie)
	
	def print_security_policies(self):
		for security_policy in self.security_policies_list:
			security_policy.print_security_policy()



class security_policy:
	def __init__(self):
		self.id = ""
		self.name=""
		self.description=""
		self.objective=""
	
	def set_id(self, id):
		self.id = id
	
	def set_name(self, name):
		self.name = name
	
	def set_description(self, description):
		self.description = description
	
	def set_objective(self, objective):
		self.objective = objective
	
	def print_security_policy(self):
		t = (self.id, self.name, self.description, self.objective)
		print(t)
	
	
class security_relationships:
	def __init__(self):
		self.security_relationships_list = []

	def add_security_relationship(self, security_relationship):
		self.security_relationships_list.append(security_relationship)

	def print_security_relationships(self):
		for security_relationship in self.security_relationships_list:
			security_relationship.print_security_relationship()



class security_relationship:
	def __init__(self):
		self.id=""
		self.interactions_id = []
	
	def set_id(self, id):
		self.id=id
	
	def add_interaction_id(self, interaction_id):
		self.interactions_id.append(interaction_id)

	def print_security_relationship(self):
		t = (self.id, self.interactions_id)
		print(t)


