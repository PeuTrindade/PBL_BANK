from flask import Flask, request, jsonify
from controllers.ClientController import ClientController

app = Flask(__name__)

@app.route('/client', methods=['POST'])
def createClient():
    try:
        requestBody = request.json
        
        name = requestBody.get('name')
        email = requestBody.get('email')
        age = requestBody.get('age')
        
        controllerResponse = ClientController.create(name=name, email=email, age=age)
        
        if controllerResponse['ok']:
            return jsonify({ "message": controllerResponse['message'] }), 201
        else:
            return jsonify({ "message": controllerResponse['message'] }), 400
    except:
        return jsonify({ "message": "Ocorreu um erro interno!" }), 500
    
@app.route('/client', methods=['get'])
def listClients():
    try:
        clients = ClientController.list()
        
        print(clients)
        
        return jsonify({ "clients": clients['clients'] }), 200
    except:
        return jsonify({ "message": "Ocorreu um erro interno!" }), 500

if __name__ == '__main__':
    app.run(debug=True)