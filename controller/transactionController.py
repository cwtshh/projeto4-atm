from datetime import datetime
import json

from model.transaction import Transaction


class TransactionController:

    # construtor da classe TransactionController
    def __init__(self, transactionList, directory):
        self.transactionList = transactionList
        self.directory = directory

    # atualiza o banco de dados
    def updateJson(self, conta, transactions):
        with open(f"projeto4-atm\\database\\transactions\\extratos_{conta}.json", "w") as updateFile:
            json.dump(transactions, updateFile, indent=4)

        updateFile.close()

    # cria uma nova transação e adiciona no banco de dados
    def newTransaction(self, type, conta, value):
        date = str(datetime.now())

        transaction = Transaction(type, conta, value, date)
        convertedTransaction = vars(transaction)

        with open(f"projeto4-atm\\database\\transactions\\extratos_{conta}.json") as transactionsFile:
            transactions = json.load(transactionsFile)
        transactions.append(convertedTransaction)

        self.updateJson(conta, transactions)
        
        transactionsFile.close()
    

        """ self.transactionList.append(convertedTransaction)

        self.updateJson() """

    # mostra as transações
    def showTransactions(self, account):
        with open(f"projeto4-atm\\database\\transactions\\extratos_{account}.json") as transactionsFile:
            transactions = json.load(transactionsFile)

        for transaction in transactions:
            
            if transaction['conta'] == account:
                print(f"Tipo: {transaction['type']} \nConta: {transaction['conta']} \nValor: {transaction['value']} \nData: {transaction['date']}\n")


            

