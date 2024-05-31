from flask import Flask, request, jsonify
from controllers.ClientController import ClientController
from controllers.AccountController import AccountController
import socket

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
        
    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500
    

@app.route('/client', methods=['GET'])
def listClients():
    try:
        clients = ClientController.list()
        
        return jsonify({ "clients": clients['clients'] }), 200
    
    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500

  
@app.route('/account', methods=['POST'])
def createAccount():
    try:
        requestBody = request.json
        
        clientIds = requestBody.get('clientIds')
        accountType = requestBody.get('accountType')
        agency = requestBody.get('agency')
        accountPass = requestBody.get('accountPass')
        
        controllerResponse = AccountController.create(clientIds, accountType, agency, accountPass)
        
        if controllerResponse['ok']:
            return jsonify({ "message": controllerResponse['message'] }), 201
        else:
            return jsonify({ "message": controllerResponse['message'] }), 400
        
    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500


@app.route('/account', methods=['GET'])
def listAccounts():
    try:
        accounts = AccountController.list()
        
        return jsonify({ "accounts": accounts['accounts'] }), 200
    
    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500
    

@app.route('/account/auth', methods=['POST'])
def authAccount():
    try:
        requestBody = request.json
 
        accountPass = requestBody.get('accountPass')
        verifyAuth = AccountController.auth(accountPass)

        if verifyAuth['ok'] == False:
            return jsonify({ "message": verifyAuth['message'] }), 400
        
        return jsonify({ "account": verifyAuth['account'] }), 200

    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500


@app.route('/account/transfer/<string:fromAccountPass>', methods=['POST'])
def transfer(fromAccountPass):
    try:
        requestBody = request.json
 
        toAccountPass = requestBody.get('to')
        value = requestBody.get('amount')
        toAgency = requestBody.get('agency')

        controllerResponse = AccountController.transfer(fromAccountPass, toAccountPass, toAgency, value)

        if controllerResponse['ok'] == False:
            return jsonify({ "message": controllerResponse['message'] }), 400
        
        return jsonify({ "account": controllerResponse['message'] }), 200

    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500
    

@app.route('/account/deposit/<string:accountPass>', methods=['PATCH'])
def deposit(accountPass):
    try:
        requestBody = request.json
        amount = requestBody.get('amount')

        controllerResponse = AccountController.deposit(accountPass, amount)

        if controllerResponse['ok'] == False:
            return jsonify({ "message": controllerResponse['message'] }), 400
        
        return jsonify({ "account": controllerResponse['message'] }), 200

    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500

   
@app.route('/account/withdraw/<string:accountPass>', methods=['PATCH'])
def withdraw(accountPass):
    try:
        requestBody = request.json
        amount = requestBody.get('amount')

        controllerResponse = AccountController.withdraw(accountPass, amount)

        if controllerResponse['ok'] == False:
            return jsonify({ "message": controllerResponse['message'] }), 400
        
        return jsonify({ "account": controllerResponse['message'] }), 200

    except Exception as e:
        return jsonify({ "message": "Ocorreu um erro interno: " + str(e)  }), 500


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    port = int(ip_address.split(".")[-1]) * 2000

    app.run(host='0.0.0.0', port=port, debug=True)