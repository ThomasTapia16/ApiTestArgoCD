from fastapi import APIRouter, HTTPException, Path, Depends
from .config import SessionLocal
from sqlalchemy.orm import Session
from .schemas import PersonaSchema, RequestPersona, Response
from . import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
def create(request:RequestPersona, db:Session=Depends(get_db)):
    crud.create_Persona(db, request.parameter)
    return Response(code=200, status='ok',message="creado correctamente").dict(exclude_none=True)


@router.get('/')
def get_all(db:Session=Depends(get_db)):
    _persona = crud.get_Persona(db, 0, 100)
    return Response(code=200, status='ok',message="Fetch all data", result=_persona).dict(exclude_none=True)


@router.get('/{rut}')
def get_by_id(rut:str, db:Session=Depends(get_db)):
    _persona = crud.get_Persona_by_rut(db, rut)
    return Response(code=200, status='ok',message="encontrado", result=_persona).dict(exclude_none=True)