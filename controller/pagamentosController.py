import json
from model.pagamentoProgramado import PagamentoProgramado
from datetime import datetime

class pagamentosController:
    
    def __init__(self, paymentDirectory, userController, transactionController):
        self.paymentDirectory = paymentDirectory
        self.userController = userController
        self.transactionController = transactionController

    def updatePayments(self, paymentList):
        with open(self.paymentDirectory, "w") as paymentFile:
            json.dump(paymentList, paymentFile, indent=4)


    def checkForPayments(self):
        with open(self.paymentDirectory) as paymentFile:
            paymentList = json.load(paymentFile)

        if paymentFile == []:
            return "Não há pagamentos agendados"
        
        else:
            return paymentList
        
    def addPayment(self, valor, conta, data):
        newPayment = PagamentoProgramado(valor, conta, data)
        convertedPayment = vars(newPayment)
        paymentList = self.checkForPayments()
        paymentList.append(convertedPayment)
        self.updatePayments(paymentList)

    def makePayment(self):
        paymentList = self.checkForPayments()
        
        for payment in paymentList:
            if payment['date'] == datetime.now():

                # fazer o pagamento
                self.userController.withdraw(payment['value'], payment['account'])
                self.transactionController.newTransaction("Pagamento", payment['account'], payment['value'])

                # remove o pagamento da lista
                paymentList.remove(payment)
                self.updatePayments(paymentList)

