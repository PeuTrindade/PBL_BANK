from entities.Client import Client
from database.database import database

class ClientModel:
    @staticmethod
    def create(name, email, age):
        newClient = Client(name, email, age)
        
        database['clients'].append(newClient.transformToDic())