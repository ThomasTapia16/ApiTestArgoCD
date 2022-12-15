from sqlalchemy import Column, String
from .config import Base


class Persona(Base):
    __tablename__= 'Persona'
    rut = Column(String, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)