from sqlalchemy import Column,types,ForeignKey
from base_de_datos import conexion

class EmpleadoModel(conexion.Model):
    id = Column(type_=types.Integer , primary_key=True , autoincrement = True)
    nombre = Column(type_=types.Text , nullable=False)
    apellido = Column(type_=types.Text , nullable=False)
    email = Column(type_=types.Text , nullable=False)
    areaId = Column(ForeignKey(column='areas.id'), nullable=False, name='area_id')
    __tablename__ = 'empleados'

    