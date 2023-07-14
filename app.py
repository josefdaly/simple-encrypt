from flask import Flask, request, abort
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return 'Hello World'

@app.route("/get-key", methods=['GET'])
def generate_key():
    return Fernet.generate_key()

@app.route("/encode", methods=['GET'])
def encode():
    key = request.args['key']
    message = request.args['message']
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

@app.route("/decode", methods=['GET'])
def decode():
    key = request.args['key']
    message = request.args['message']
    fernet = Fernet(key)
    return fernet.decrypt(message).decode()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
