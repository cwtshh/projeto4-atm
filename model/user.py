class User:
    def __init__(self, name, cpf, password):
        self.name = name
        self.cpf = cpf
        self.password = password

    def getName(self):
        return self.name
    
    def getCpf(self):
        return self.cpf
    
    def getPassword(self):
        return self.password
    
    def setName(self, name):
        self.name = name

    def setCpf(self, cpf):
        self.cpf = cpf

    def setPassword(self, password):
        self.password = password