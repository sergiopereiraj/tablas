from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate #migracion bd
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required #para autenticacion (el que dice ser)
from flask_cors import CORS #ayuda a informar de que sitios web pueden consultar la api
from werkzeug.security import generate_password_hash, check_password_hash #encriptacion de contraseña
from models import db 

app = Flask(__name__)
app.url_map.strict_slashes = False #que si el usuario usa / o no, no afecte el funcionamiento
app.config['DEBUG']= True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #nombre base de dato
app.config['JWT_SECRET_KEY'] = '0b97c0b28c1515ad6767f009e505873a'
db.init_app(app) #vinculando bd con objeto db
Migrate(app, db) # db init, db migrate, db upgrade, db downgrade
jwt = JWTManager(app)
CORS(app)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()