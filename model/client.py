class Client():

    def __init__(self, name, cpf, password, account, money):
        self.name = name
        self.cpf = cpf
        self.password = password
        self.account = account
        self.money = money

    def getAccount(self):
        return self.account
    
    def getMoney(self):
        return self.money
    