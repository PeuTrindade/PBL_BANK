from models.AccountModel import AccountModel
from database.database import database
import socket

class AccountController:
    @staticmethod
    def create(clientIds, accountType, agency, accountPass):
        if (clientIds == None or accountType == None or agency == None or accountPass == None):
            return { "message": "Campos em branco foram enviados", "ok": False }
        
        elif AccountModel.accountExists(accountPass) == True:
            return { "message": "Conta já cadastrada com este código!", "ok": False }

        AccountModel.create(clientIds, accountType, agency, accountPass)
        
        return { "message": "Conta cadastrada com sucesso!", "ok": True }
    
    @staticmethod
    def list():
        return { "accounts": database['accounts'] }
    
    @staticmethod
    def auth(accountPass):
        account = AccountModel.findByAccountPass(accountPass)

        if account:
            return { "account": account, "ok": True }
        
        return { "message": "Conta não existente!", "ok": False }
    
    @staticmethod
    def transfer(fromAccountPass, toAccountPass, toAgency, value):
        fromAccount = AccountModel.findByAccountPass(fromAccountPass)
        toAccount = AccountModel.findByAccountPass(toAccountPass)

        if fromAccount:
            if float(fromAccount['balance']) >= float(value):
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                agency = ip_address.split(".")[-1]

                if str(toAgency) == str(agency):
                    if toAccount:
                        isTransferSucess = AccountModel.transfer(accountPass=fromAccountPass, value=value)
                        isReceiveSuccess = AccountModel.receive(accountPass=toAccountPass, value=value)

                        if isTransferSucess and isReceiveSuccess:
                            return { "message": "Transferência realizada com sucesso!", "ok": True }
                        else:
                            if isTransferSucess == False:
                                return { "message": "Erro na transferência!", "ok": False }
                            
                            return { "message": "Erro no recebimento!", "ok": False }
                    else:
                        return { "message": "Conta destino não encontrada!", "ok": False }
                else:
                    return { "message": "Transferência realizada para outro banco com sucesso!", "ok": True }
            else:
                return { "message": "Saldo insuficiente!", "ok": False }
        
        else:
            return { "message": "Conta remetente não encontrada!", "ok": False }
        
    @staticmethod
    def deposit(accountPass, amount):
        account = AccountModel.findByAccountPass(accountPass)

        if account:
            AccountModel.deposit(accountPass, amount)
            
            return { "message": "Depósito realizado com sucesso!", "ok": True }

        return { "message": "Conta não encontrada!", "ok": False }