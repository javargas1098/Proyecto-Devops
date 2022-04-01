from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from vistas import VistaLogIn, VistaSignIn, VistaBlackList, VistaHealth,VistaBlackListDetail

from modelos import db


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgresql:postgresql@postgresql.cjvfvqpbuza0.us-east-1.rds.amazonaws.com:5432/postgresql"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)

api.add_resource(VistaSignIn, '/api/auth/signup')
api.add_resource(VistaLogIn, '/api/auth/login')
api.add_resource(VistaBlackList, '/api/black-list')
api.add_resource(VistaBlackListDetail, '/api/black-list/<string:email>')
api.add_resource(VistaHealth, '/api/health/ping')


jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3020)
