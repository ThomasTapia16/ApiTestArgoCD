from sqlalchemy.orm import Session
from .model import Persona
from .schemas import PersonaSchema

def get_Persona(db: Session, skip:int=0, limit:int=100):
    return db.query(Persona).offset(skip).limit(limit).all()
def get_Persona_by_rut(db: Session, rut: str):
    return db.query(Persona).filter(Persona.rut == rut).first()

def create_Persona(db: Session, persona: PersonaSchema):
    _persona = Persona(rut=persona.rut, nombre=persona.nombre,apellido = persona.apellido)
    db.add(_persona)
    db.commit()
    db.refresh(_persona)
    return _persona
