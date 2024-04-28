from fastapi import FastAPI
from sqlmodel import SQLModel,Field,select,create_engine,Session

app = FastAPI()


connection_string ="postgresql://postgres.dhrehaxissxxbgsmqtfs:2BwcgpbFnVg0LMD5@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"
engine = create_engine(connection_string)

class Todos(SQLModel,table=True):
    id:int =Field(primary_key=True)
    name:str = Field()
    completed:bool = Field(default=False)

SQLModel.metadata.create_all(engine)

@app.get("/getodos")
def todos():
    with Session(engine) as session:
        todos = session.exec(select(Todos)).all()
        return todos
    
# @app.post("/settodo")
# # def set_todo():
# #     with Session(engine) as session:
# #         session.s