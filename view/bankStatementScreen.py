from controller.transactionController import TransactionController

class BankStatementScreen:
    def __init__(self, user, transactionController):
        self.user = user
        self.transactionController = transactionController
        print("#---------------------------------#")
        print(f"# Extrato de {user['name']}")
        print("#                                 #")
        print("#---------------------------------#")
        transactionController.showTransactions(user['account'])
