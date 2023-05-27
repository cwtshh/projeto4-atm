from view.balanceScreen import BalanceScreen
from view.withdrawScreen import WithdrawScreen
from view.depositScreen import DepositScreen
from view.transferScreen import TransferScreen
from view.transferValueScreen import TransferValueScreen


from controller.userController import UserController
from controller.transactionController import TransactionController


class MenuScreen:

    def __init__(self, user, userController, transactionController):
        self.userController = userController
        self.transactionController = transactionController
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
        
        # SALDO
        if option == 1:
            BalanceScreen(self.user)
            answer = input("Deseja realizar outra operação? (s/n) ")
            if(answer == "s"):
                MenuScreen(self.user, self.userController, self.transactionController)
                self.selectMenuFunction()
            else:
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        # SAQUE
        if option == 2:
            WithdrawScreen(self.user)

            # Saca o valor da conta
            value = int(input("Digite o valor a ser sacado: "))
            self.userController.withdraw(value, self.user)

            # cria uma nova transacao
            self.transactionController.newTransaction("Saque", self.user['account'], value)

            print("#---------------------------------#")
            print("#Saque realizado com sucesso!     #")
            print("#---------------------------------#")

            answer = input("Deseja realizar outra operação? (s/n) ")

            if(answer == "s"):
                MenuScreen(self.user, self.userController, self.transactionController)
                self.selectMenuFunction()
            else:
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        # DEPÓSITO
        if option == 3:
            DepositScreen()

            value = int(input("Digite o valor a ser depositado: "))
            self.userController.deposit(value, self.user)

            self.transactionController.newTransaction("Deposito", self.user['account'], value)

            print("#---------------------------------#")
            print("#Depósito realizado com sucesso!  #")
            print("#---------------------------------#")

            answer = input("Deseja realizar outra operação? (s/n) ")

            if answer == "s":
                MenuScreen(self.user, self.userController, self.transactionController)
                self.selectMenuFunction()
            else:
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        # TRANSFERÊNCIA
        if option == 4:
            TransferScreen()
            transferAccount = input("Digite a conta para qual deseja transferir: ")

            for user in self.userController.userList:
                if user['account'] == transferAccount:
                    print(user['name'] + " encontrado(a)!")

                    TransferValueScreen()

                    value = int(input())
                    self.userController.transfer(value, self.user, transferAccount)

                    self.transactionController.newTransaction("Transferencia", self.user['account'], value)


        # SAIR
        if option == 5:
            print("Tem certeza que deseja sair? (s/n)")
            answer = input()

            if answer == "s":
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")



            
