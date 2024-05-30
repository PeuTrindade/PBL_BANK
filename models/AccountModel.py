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
