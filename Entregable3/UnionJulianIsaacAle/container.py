class Node:
#Inicializador, hay que agregar una variable para cada parte
    def __init__(self):
        self.id=""
        self.threats= Threats()
#Metodos set de nodos, aqui hay que agregar un set para cada parte
    def setId(self, id):
        self.id = id
    def setThreats(self, threats):
        self.threats = threats
#Print all, hay que agregar un print para cada parte para probarla
    def printAll(self):
        print("IMPRESION DE NODO")
        print("ID NODO= "+self.id)
        print("LISTA DE THREATS:")
        self.threats.printThreats()
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


"""#Metodos para testear clases
test = Threat()
testB = Threat()
test.setAll("A1","NameA1","HereGoesDescription","Vulnerability")
testB.setAll("B2","NameB2","B2HereGoesDescription","B2Vulnerability")
testThreats = Threats()
testThreats.addThreat(test)
testThreats.addThreat(testB)
testThreats.printThreats()
nodeTest = Node("Nodo A")
nodeTest.setThreat(testThreats)
nodeTest.printAll()
"""