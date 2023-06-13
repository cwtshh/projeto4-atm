from datetime import datetime

from view.balanceScreen import BalanceScreen
from view.withdrawScreen import WithdrawScreen
from view.depositScreen import DepositScreen
from view.transferScreen import TransferScreen
from view.transferValueScreen import TransferValueScreen
from view.bankStatementScreen import BankStatementScreen


from controller.userController import UserController
from controller.transactionController import TransactionController
from controller.pagamentosController import pagamentosController


class MenuScreen:

    # contrutor da classe MenuScreen
    # Recebe os controllers para fazer a comunicação com o banco de dados
    def __init__(self, user, userController, transactionController, pagamentosController):
        self.userController = userController
        self.transactionController = transactionController
        self.user = user
        self.pagamentosController = pagamentosController
        print("#---------------------------------#")
        print("# Bem vindo(a), " + user['name'] + "!")
        print("# Selecione uma opção:            #")
        print("# 1 - Saldo                       #")
        print("# 2 - Saque                       #")
        print("# 3 - Depósito                    #")
        print("# 4 - Transferência               #")
        print("# 5 - Extrato                     #")
        print("# 6 - Pagamento Agendado          #")
        print("# 7 - Sair                        #")
        print("#---------------------------------#")

    # seleciona a opcão do menu
    def selectMenuFunction(self):
        option = int(input("Digite a opção desejada: "))
        
        # SALDO
        if option == 1:

            # mostra a tela de saldo
            BalanceScreen(self.user)

            # Checa se o usuario quer realizar outra operação
            answer = input("Deseja realizar outra operação? (s/n) ")

            # Faz a logica relacionada
            if(answer == "s"):

                # chama o menu novamente pra gerar um loop nas telas do programa
                MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                self.selectMenuFunction()
            else:

                # sai do programa
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        # SAQUE
        if option == 2:

            # Mostra a tela de saque
            WithdrawScreen(self.user)

            # Pergunta ao usuario o valor que deseja sacar e chama a funcao de saque
            value = int(input("Digite o valor a ser sacado: "))
            self.userController.withdraw(value, self.user)

            # Cria uma nova transação e joga no banco de dados
            self.transactionController.newTransaction("Saque", self.user['account'], value)

            # Informa o usuario que a transação foi realizada com sucesso
            print("#---------------------------------#")
            print("#Saque realizado com sucesso!     #")
            print("#---------------------------------#")

            # Checa se o usuario quer realizar outra operação
            answer = input("Deseja realizar outra operação? (s/n) ")

            # Faz a logica relacionada
            if(answer == "s"):
                MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                self.selectMenuFunction()
            else:
                # sai do programa
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        # DEPÓSITO
        if option == 3:

            # Mostra a tela de depósito
            DepositScreen()

            # Pergunta ao usuario o valor que deseja depositar e chama a funcao de deposito
            value = int(input("Digite o valor a ser depositado: "))

            # Chama a funcao de deposito
            self.userController.deposit(value, self.user)

            # Cria uma nova transação e joga no banco de dados
            self.transactionController.newTransaction("Deposito", self.user['account'], value)

            # Informa o usuario que a transação foi realizada com sucesso
            print("#---------------------------------#")
            print("#Depósito realizado com sucesso!  #")
            print("#---------------------------------#")

            # Checa se o usuario quer realizar outra operação
            answer = input("Deseja realizar outra operação? (s/n) ")

            # Faz a logica relacionada
            if answer == "s":
                # chama o menu novamente pra gerar um loop nas telas do programa
                MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                self.selectMenuFunction()

            else:
                # sai do programa
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")


        # TRANSFERÊNCIA
        if option == 4:
            
            # Mostra a tela de transferência
            TransferScreen()

            # Pergunta ao usuario a conta que deseja transferir e chama a funcao de transferencia
            transferAccount = input("Digite a conta para qual deseja transferir: ")

            # Checa se a conta existe
            for user in self.userController.userList:
                if user['account'] == transferAccount:
                    print(user['name'] + " encontrado(a)!")

                    # Mostra a tela de transferência
                    TransferValueScreen()

                    # Pergunta ao usuario o valor que deseja transferir e chama a funcao de transferencia
                    value = int(input())
                    self.userController.transfer(value, self.user, transferAccount)

                    # Cria uma nova transação e joga no banco de dados
                    self.transactionController.newTransaction("Transferencia", self.user['account'], value)


        if option == 5:

            # Mostra a tela de extrato
            BankStatementScreen(self.user, self.transactionController)

            # Checa se o usuario quer realizar outra operação
            answer = input("Deseja realizar outra operação? (s/n) ")

            # Faz a logica relacionada
            if(answer == "s"):
                # chama o menu novamente pra gerar um loop nas telas do programa
                MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                self.selectMenuFunction()

            else:
                # sai do programa
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

        #pagamento agendado
        if option == 6:
            print("#---------------------------------#")
            print("# Pagamento Agendado              #")
            print("# 1 - Agendar                     #")
            print("# 2 - Ver pagamentos agendados    #")
            print("# 3 - Voltar                      #")
            print("#---------------------------------#")

            option = int(input("Digite a opção desejada: "))
            if option == 1:
                valor = int(input("Digite o valor a ser pago: "))
                pagamentosController.addPayment(valor, self.user['account'], datetime.now())
                print("Pagamento agendado com sucesso!")
                
                answer = input("Deseja realizar outra operação? (s/n) ")
                if answer == "s":
                    MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                    self.selectMenuFunction()

                else:
                    # sai do programa
                    print("Obrigado por utilizar nossos serviços!")
                    exit("Saindo...")

            if option == 2:
                paymentList = pagamentosController.checkForPayments()

                for payment in paymentList:
                    print(f"Valor: {payment['value']} \n Conta: {payment['account']} \n Data: {payment['date']} \n")

                answer = input("Deseja realizar outra operação? (s/n) ")
                if answer == "s":
                    MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                    self.selectMenuFunction()

                else:
                    # sai do programa
                    print("Obrigado por utilizar nossos serviços!")
                    exit("Saindo...")

            if option == 3:
                MenuScreen(self.user, self.userController, self.transactionController, self.pagamentosController)
                self.selectMenuFunction()



        # SAIR
        if option == 7:
            # Checa se o usuario quer mesmo sair
            print("Tem certeza que deseja sair? (s/n)")
            answer = input()

            if answer == "s":
                # sai do programa
                print("Obrigado por utilizar nossos serviços!")
                exit("Saindo...")

            else:
                # chama o menu novamente pra gerar um loop nas telas do programa
                MenuScreen(self.user, self.userController, self.transactionController)



            
