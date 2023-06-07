import json
from view.logScreen import LogScreen
from view.passScreen import PassScreen
from view.menuScreen import MenuScreen

from controller.userController import UserController
from controller.transactionController import TransactionController




userDirectory = "projeto4-atm\\database\\users.json"
transactionDirectory = "projeto4-atm\\database\\transactions.json"

if __name__ == "__main__":

    LoggedUser = None

    with open(userDirectory) as fp:
        usersList = json.load(fp)

    with open(transactionDirectory) as fp:
        transactionsList = json.load(fp)

    userController = UserController(usersList, userDirectory)
    userController.printUsers()

    transactionController = TransactionController(transactionsList, transactionDirectory)




    # logic starts here
    LogScreen()
    account = input()

    if account == "0001":
        print("Cadastrar usuario")
        name = input("Nome: ")
        cpf = input("CPF: ")
        password = input("Senha: ")
        account = input("Conta: ")
        money = int(input("Dinheiro: "))

        userController.registerUser(name, cpf, password, account, money)
        exit("Usuario criado com sucesso!")


    if userController.checkAccount(account) == 0:
        print("Conta não encontrada")
        exit()

    PassScreen()
    password = input()

    if userController.logUser(account, password) == None:
        print("Senha incorreta")
        exit()

    LoggedUser = userController.logUser(account, password)

    menu = MenuScreen(LoggedUser, userController, transactionController)

    menu.selectMenuFunction()

    #print(LoggedUser)



    

    




