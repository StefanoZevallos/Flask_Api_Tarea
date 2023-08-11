from models.area import AreaModel
from flask_restful import Resource, request
from base_de_datos import conexion
from dtos.area import AreaRequestDTO
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

class AreasController(Resource):
    def get(self):
        usuarios = conexion.session.query(AreaModel).all()
        dto = AreaRequestDTO()
        resultado = dto.dump(usuarios,many=True)

        return resultado
    
class AreaController(Resource):

    def post(self):
        data=request.json
        dto = AreaRequestDTO()
        try:
            dataValidada = dto.load(data)
            nuevaArea = AreaModel(**dataValidada)
            conexion.session.add(nuevaArea)
            conexion.session.commit()

            return {
                'message' : 'Area Insertada Correctamente'
            }, 201
        
        except ValidationError as error:
            return {
                'message':'Error al crear el área',
                'error':error.args
            },400
        
        except IntegrityError as error:
            return {
                'message':'Error al crear el area',
                'error':'El area ya existe'
            },400
        
        except Exception as error:
            return {
                'message':'Error al crear el area',
                'error': error.args
            },400    

class AreaControllerGet(Resource):
     def get(self,id):
         areaEcontrada = conexion.session.query(AreaModel).filter_by(id=id).first()
         if not areaEcontrada:
             return {
                 'message': 'El usuario no existe'
             }, 404
        
         dto = AreaRequestDTO()
         areaConvertida = dto.dump(areaEcontrada)

         return areaConvertida            