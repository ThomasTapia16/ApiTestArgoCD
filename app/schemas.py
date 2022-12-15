from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


T = TypeVar('T')

class PersonaSchema(BaseModel):
    rut: Optional[str]=None
    nombre: Optional[str]=None
    apellido: Optional[str]=None

    class config:
        orm_mode=True
class RequestPersona(BaseModel):
    parameter: PersonaSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]