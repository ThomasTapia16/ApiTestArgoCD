from typing import Union

from fastapi import FastAPI
import os
from .config import engine
from . import model
from .router import router

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)