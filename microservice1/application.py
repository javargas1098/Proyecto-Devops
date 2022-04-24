from email.mime import application
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from vistas import VistaLogIn, VistaSignIn, VistaBlackList, VistaHealth,VistaBlackListDetail

from modelos import db


def create_app(config_name):
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgresql:postgresql@postgresql.cjvfvqpbuza0.us-east-1.rds.amazonaws.com:5432/postgresql"
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    application.config['JWT_SECRET_KEY'] = 'frase-secreta'
    application.config['PROPAGATE_EXCEPTIONS'] = True
    return application


application = create_app('default')
app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()
cors = CORS(application)

api = Api(application)

api.add_resource(VistaSignIn, '/api/auth/signup')
api.add_resource(VistaLogIn, '/api/auth/login')
api.add_resource(VistaBlackList, '/api/black-list')
api.add_resource(VistaBlackListDetail, '/api/black-list/<string:email>')
api.add_resource(VistaHealth, '/api/health/ping')


jwt = JWTManager(application)

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True, port=3020)
