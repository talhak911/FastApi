from sqlmodel import create_engine,SQLModel,Field,Session,select
import os
connection_string=os.getenv("DB_URI")
engine = create_engine(connection_string)

def create_table():
    SQLModel.metadata.create_all(engine)