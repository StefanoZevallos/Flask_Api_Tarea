from models.empleado import EmpleadoModel
from flask_restful import Resource, request
from base_de_datos import conexion
from dtos.empleado import EmpleadoRequestDTO
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

class EmpleadoController(Resource):
    def post(self):
        data=request.json
        dto = EmpleadoRequestDTO()
        try:
            dataValidada = dto.load(data)
            nuevoEmpleado = EmpleadoModel(**dataValidada)
            conexion.session.add(nuevoEmpleado)
            conexion.session.commit()

            return {
                'message' : 'Empleado Insertado Correctamente'
            }, 201
        
        except ValidationError as error:
            return {
                'message':'Error al crear el empleado',
                'error':error.args
            },400
        
        except IntegrityError as error:
            return {
                'message':'Error al crear el empleado',
                'error':'El area ya existe'
            },400
        
        except Exception as error:
            return {
                'message':'Error al crear el empleado',
                'error': error.args
            },400 

class EmpleadoControllerGet(Resource):
    def get(self):
        query_params = request.args
        print(query_params)

        try:
            if "email" in query_params:
                empleados_filtrados = EmpleadoModel.query.filter_by(email=query_params["email"]).all()
            elif "nombre" in query_params:
                empleados_filtrados = EmpleadoModel.query.filter_by(nombre=query_params["nombre"]).all()
            else:
                empleados_filtrados = EmpleadoModel.query.all()

        
        except Exception as error:
            return {
                'message': 'Error al obtener los empleados',
                'error': error.args
            }, 400
        
        dto = EmpleadoRequestDTO()
        empleadoConvertido = dto.dump(empleados_filtrados,many=True)
        return empleadoConvertido
        