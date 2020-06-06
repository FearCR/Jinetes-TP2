
class Node:
#Initializer method
    def __init__(self,id):
        self.id=id
        self.threats= Threats()
#Set method for node members
    def setThreat(self, threats):
        self.threats = threats
#Print all, aqui iria prints de todo cuando esten listos
    def printAll(self):
        print("ID= "+self.id)
        print("Threats:")
        self.threats.printThreats()

class Threats:
#Initializer method
    def __init__(self):
        self.threatList=[]
#Method to add new Threat to list
    def addThreat(self,threat):
        self.threatList.append(threat)
#Print method
    def printThreats(self):
        for threat in self.threatList:
            threat.printThreat()

#Class Threat stores the data from each individual threat
class Threat:
#Initializer method
    def __init__(self):
        self.id=""
        self.name=""
        self.description=""
        self.vulnerability=""
#Test method to set all variables at once
    def setAll(self,newID,newName,newDescription,newVulnerability):
        self.id=newID
        self.name=newName
        self.description=newDescription
        self.vulnerability=newVulnerability
#Set methods for threat
    def setId(self,newID):
        self.id=newID

    def setName(self,newName):
        self.name=newName

    def setDescription(self,newDescription):
        self.description=newDescription

    def setVulnerability(self,newVulnerability):
        self.vulnerability=newVulnerability
#Print method to view stored data
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
