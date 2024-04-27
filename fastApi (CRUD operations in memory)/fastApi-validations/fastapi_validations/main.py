from fastapi import FastAPI,Path,Query,Body
from typing import Annotated
from pydantic import BaseModel,Field
import uvicorn

class formType(BaseModel):
    name:str=Field(min_length=3)
    age:int=Field(ge=18)

app = FastAPI()
@app.get("/")
def home():
    return {"Message":"return from home page"}

@app.post("/addbybody")
def addStudent(data:formType):
    return "added"


@app.post("/addbyparams")
def add_by_params(name:Annotated[str,Query(min_length=3)]):
    return "added"

@app.post("/addbypath/{path}")
def add_by_path_variable(path:Annotated[int,Path(le=10)]):
    return "added"

@app.post("/addbypathandparam/{path}")
def add_by_path_param(path:Annotated[int,Path(le=10)] , name:Annotated[str,Query(min_length=3)]):
    return "added"

def start():
    uvicorn.run("fastapi_validations.main:app",host="127.0.0.1",port=8080, reload=True)
