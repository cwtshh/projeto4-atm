import json

class UserController:

    # construtor da classe UserController
    def __init__(self, userList, directory):
        self.userList = userList
        self.directory = directory

    # imprime os usuarios
    def printUsers(self):
        for user in self.userList:
            print(user)

    # checa se a conta existe
    def checkAccount(self, account):
        for user in self.userList:
            if account == user['account']:
                return 1
        return 0
    
    # checa se a conta e a senha estao corretas
    def logUser(self, account, password):
        for user in self.userList:
            if user['account'] == account and user['password'] == password:
                return user      
        return None
    
    # atualiza o json
    def updateJson(self):
        with open(self.directory, "w") as updateFile:
            json.dump(self.userList, updateFile, indent=4)
    

    # função de saque
    def withdraw(self, value, loggedUser):
        for user in self.userList:
            if user['account'] == loggedUser['account']:
                user['money'] -= value
                self.updateJson()

    # função deposito
    def deposit(self, value, loggedUser):
        for user in self.userList:
            if user['account'] == loggedUser['account']:
                user['money'] += value
                self.updateJson()

    # função transferencia
    def transfer(self, value, loggedUser, account):
        for user in self.userList:
            if user['account'] == loggedUser['account']:
                user['money'] -= value

                if user['account'] == account:
                    user['money'] += value
                    
                    self.updateJson()


        


            

            
            
            
                
    
                



