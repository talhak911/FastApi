from fastapi import FastAPI
import uvicorn
students =[{"name":"talha","rollNo":1},{"name":"khan","rollNo":2},{"name":"taf","rollNo":3}]
app=FastAPI()
@app.get("/")
def hello():
    return "hello"
@app.get("/students/{name}")
async def GetRollNo(name:str):
    for student in students:
        if student["name"] ==name:
            return f"Student roll no is {student['rollNo']}"
@app.post("/students/")
async def GetRollNo(name:str):
    students.append({"name":name,"rollNo":4})
    return students
def start():
    uvicorn.run("fastapiy.main:app",host="127.0.0.1",port=8080,reload=True)