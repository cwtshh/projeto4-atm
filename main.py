import json
from view.logScreen import LogScreen
from view.passScreen import PassScreen
from view.menuScreen import MenuScreen
from view.depositScreen import DepositScreen
from view.balanceScreen import BalanceScreen

from controller.userController import UserController




userDirectory = "projeto4-atm\\database\\users.json"

if __name__ == "__main__":

    LoggedUser = None

    with open(userDirectory) as fp:
        usersList = json.load(fp)

    userController = UserController(usersList, userDirectory)

    userController.printUsers()


    # logic starts here
    LogScreen()
    account = input()

    if userController.checkAccount(account) == 0:
        print("Conta não encontrada")
        exit()

    PassScreen()
    password = input()

    if userController.logUser(account, password) == None:
        print("Senha incorreta")
        exit()

    LoggedUser = userController.logUser(account, password)

    menu = MenuScreen(LoggedUser, userController)

    menu.selectMenuFunction()

    #print(LoggedUser)



    

    




