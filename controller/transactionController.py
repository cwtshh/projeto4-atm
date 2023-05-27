from datetime import datetime
import json

from model.transaction import Transaction


class TransactionController:

    def __init__(self, transactionList, directory):
        self.transactionList = transactionList
        self.directory = directory

    def updateJson(self):
        with open(self.directory, "w") as updateFile:
            json.dump(self.transactionList, updateFile, indent=4)


    def newTransaction(self, type, conta, value):
        date = str(datetime.now())

        transaction = Transaction(type, conta, value, date)
        convertedTransaction = vars(transaction)

        self.transactionList.append(convertedTransaction)

        self.updateJson()

