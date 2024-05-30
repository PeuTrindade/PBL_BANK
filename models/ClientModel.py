from entities.Client import Client
from database.database import database

class ClientModel:
    @staticmethod
    def create(name, email, age):
        newClient = Client(name, email, age)
        
        database['clients'].append(newClient.transformToDic())

    @staticmethod
    def clientExists(email):
        clients = database['clients']

        for cliente in clients:
            if cliente["email"] == email:
                return True
            
            return False
    