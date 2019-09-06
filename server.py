import connexion
from flask_cors import CORS
from flask import Flask, render_template

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')
CORS(app.app,resources=r'/api/*',methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])

@app.route('/')
def home():
    return render_template('clientes.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

