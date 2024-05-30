from models.AccountModel import AccountModel
from database.database import database

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