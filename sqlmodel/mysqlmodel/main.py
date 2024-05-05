import uvicorn
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
load_dotenv()
from sqlmodel import Session,select
from .models.todo import Todo,UpdateTodo
from mysqlmodel.config.db import engine,create_table
app = FastAPI()


@app.get("/get_todo")
def get_todo():
    with Session(engine) as session:
        todo=session.exec(select(Todo)).all()
        return todo
    
@app.post("/create_todo")
def create_todo(todo:Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return {"message":"created todo"}
    
@app.put("/update_todo/{todo_id}")
def update_todo(todo_id:int,todo:UpdateTodo):
    with Session(engine) as session:
        db_todo=session.get(Todo,todo_id)
        if not db_todo:
            raise HTTPException(status_code=404,detail="Todo not found")
        todo_data=todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update(todo_data)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"message":"updated todo"}

def start():
    create_table()
    uvicorn.run("mysqlmodel.main:app",reload=True,host="127.0.0.1",port=8000)