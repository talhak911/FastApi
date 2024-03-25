from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/")
def hello():
    return "hello"
@app.get("/students")
def hello():
    return "talha"

def start():
    uvicorn.run("fastapiy.main:app",host="127.0.0.1",port=8080,reload=True)