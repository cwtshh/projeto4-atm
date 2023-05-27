from view.balanceScreen import BalanceScreen
from view.withdrawScreen import WithdrawScreen
from view.depositScreen import DepositScreen


from controller.userController import UserController


class MenuScreen:

    def __init__(self, user, userController):
        self.userController = userController
        self.user = user
        print("#---------------------------------#")
        print("# Bem vindo(a), " + user['name'] + "!")
        print("# Selecione uma opção:            #")
        print("# 1 - Saldo                       #")
        print("# 2 - Saque                       #")
        print("# 3 - Depósito                    #")
        print("# 4 - Transferência               #")
        print("# 5 - Sair                        #")
        print("#---------------------------------#")

    def selectMenuFunction(self):
        option = int(input("Digite a opção desejada: "))
        
        if option == 1:
            BalanceScreen(self.user)
            answer = input("Deseja realizar outra operação? (s/n) ")
            if(answer == "s"):
                MenuScreen(self.user)
                self.selectMenuFunction()
            else:
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        if option == 2:
            WithdrawScreen(self.user)

            value = int(input("Digite o valor a ser sacado: "))
            self.userController.withdraw(value, self.user)

            print("#---------------------------------#")
            print("#Saque realizado com sucesso!     #")
            print("#---------------------------------#")

            answer = input("Deseja realizar outra operação? (s/n) ")

            if(answer == "s"):
                MenuScreen(self.user)
                self.selectMenuFunction()
            else:
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        if option == 3:
            DepositScreen()

            value = int(input("Digite o valor a ser depositado: "))
            self.userController.deposit(value, self.user)

            print("#---------------------------------#")
            print("#Depósito realizado com sucesso!  #")
            print("#---------------------------------#")

            answer = input("Deseja realizar outra operação? (s/n) ")

            if answer == "s":
                MenuScreen(self.user)
                self.selectMenuFunction()
            else:
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        if option == 4:
            print("Em desenvolvimento...")


            
