
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
