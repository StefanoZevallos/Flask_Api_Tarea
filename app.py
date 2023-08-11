from flask import Flask
from os import environ
from base_de_datos import conexion
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from controllers.area import AreaController,AreasController, AreaControllerGet
from controllers.empleado import EmpleadoController , EmpleadoControllerGet
from models import *

load_dotenv()
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

CORS(app, origins='*')
api = Api(app)

conexion.init_app(app)

Migrate(app, conexion)

api.add_resource(AreasController,'/areas')
api.add_resource(AreaController,'/area')
api.add_resource(AreaControllerGet,'/area/<int:id>')
api.add_resource(EmpleadoController,'/empleado')
api.add_resource(EmpleadoControllerGet,'/empleados')


# api.add_resource(AreasController, '/areas')
# api.add_resource(AreaController, '/area')

if __name__ == '__main__':
    app.run(debug=True)