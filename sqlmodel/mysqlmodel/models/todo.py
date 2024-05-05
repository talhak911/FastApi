from sqlmodel import create_engine,SQLModel,Field,Session,select
from typing import Optional
class Todo(SQLModel,table= True):
    title:str= Field()
    id:int=Field(primary_key=True)
    is_completed:bool
class UpdateTodo(SQLModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None