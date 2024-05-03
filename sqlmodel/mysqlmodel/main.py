from fastapi import FastAPI, testclient
from sqlmodel import create_engine,SQLModel,Field,Session,select


connection_string =""
engine = create_engine(connection_string)
app = FastAPI()

class students(SQLModel,table= True):
    name:str= Field()
    id:int=Field(primary_key=True)
    roll:int =Field(max_length=5)

SQLModel.metadata.create_all=(engine)


@app.get(students)
def get_students():
    with Session(engine) as session:
        students=session.exec(select(students)).all()
        return students