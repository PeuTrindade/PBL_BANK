from entities.Account import Account
from database.database import database

class AccountModel:
    @staticmethod
    def create(clientIds, accountType, agency, accountPass):
        newAccount = Account(clientIds, accountType, agency, accountPass)

        database['accounts'].append(newAccount.transformToDic())

    @staticmethod
    def accountExists(accountPass):
        accounts = database['accounts']

        for account in accounts:
            if account["accountPass"] == accountPass:
                return True
            
            return False
        
    @staticmethod
    def findByAccountPass(accountPass):
        for account in database['accounts']:
            if account["accountPass"] == accountPass:
                return account
            
        return None
    
    @staticmethod
    def transfer(accountPass, value):
        for account in database['accounts']:
            if account["accountPass"] == accountPass:
                account["balance"] -= value

                return True
            
            return False
        
    @staticmethod
    def receive(accountPass, value):
        for account in database['accounts']:
            if account["accountPass"] == accountPass:
                account["balance"] += value

                return True
            
            return False
        
    @staticmethod
    def deposit(accountPass, amount):
        for account in database['accounts']:
            if account["accountPass"] == accountPass:
                account["balance"] += amount

                return True
            
            return False

