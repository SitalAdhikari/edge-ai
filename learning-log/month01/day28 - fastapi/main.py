import json
from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

@app.get('/')
def greet():
	return "Hello, I am learning FastAPI"

def load_data():
	with open('students.json','r') as file:
		return json.load(file)

@app.get('/students')
def all_students():
	return load_data()

@app.get('/students/{student_id}') #student_id is the path parameter here
def student_id(
		student_id:str = Path(..., description = "The ID of the students", examples=['SOO1'])
	): # = Path(...) it means path is compulsory , # str - automated typechecking
	data = load_data()
	
	if student_id not in data:
		raise HTTPException(
			status_code=404,
			detail = f"Student with Id {student_id} not found"
		)
	
	return data[student_id]
	
'''	
QUERY:
http://127.0.0.1:8000/filter?course=Python

'''

@app.get('/filter')
def filter_student(course:str):
	data = load_data()
	
	if course not in data:
		return data
	
