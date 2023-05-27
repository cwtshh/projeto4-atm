import json

class UserController:
    def __init__(self, userList, directory):
        self.userList = userList
        self.directory = directory

    def printUsers(self):
        for user in self.userList:
            print(user)


    def checkAccount(self, account):
        for user in self.userList:
            if account == user['account']:
                return 1
        return 0
    

    def logUser(self, account, password):
        for user in self.userList:
            if user['account'] == account and user['password'] == password:
                return user      
        return None
    
    def updateJson(self):
        with open(self.directory, "w") as updateFile:
            json.dump(self.userList, updateFile, indent=4)
    

    
    def withdraw(self, value, loggedUser):
        for user in self.userList:
            if user['account'] == loggedUser['account']:
                user['money'] -= value
                self.updateJson()

    def deposit(self, value, loggedUser):
        for user in self.userList:
            if user['account'] == loggedUser['account']:
                user['money'] += value
                self.updateJson()
            

            
            
            
                
    
                



