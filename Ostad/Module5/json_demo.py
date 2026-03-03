import datetime as dt
import json
student ={
    "name":"Sadrul Amin",
    "age": 22,
    "date" : dt.datetime.now(),
}
print(student)
print(type(student))

j_student = json.dumps(student, default=str) #default=str: to convert non-serializable objects to string
print(j_student)
print(type(j_student))

p_student=json.loads(j_student)
print(p_student)
print(type(p_student))