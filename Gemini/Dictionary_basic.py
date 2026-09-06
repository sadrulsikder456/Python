student={}
student['name']=str(input("Enter your name:"))
student['age']=int (input("Enter your age:"))
student['department']=str(input("Enter your department:"))
student['CGPA']=float(input("Enter your CGPA:"))
print("Student details are:",student)

#TODO: dictonary ar keys ar sathe value ak sathe dekhai like protitar sathe sathei ooitar value dekhai
for i in student:
    print(i,":",student[i])

#TODO: dictonary ar khali keys gula dekhabe like name, age, department, CGPA
for i in student.keys():
    print(i)


#TODO: dictonary ar khali values gula dekhabe like "Sadrul", 24, "Computer Science & Engineering", 3.36
for i in student.values():
    print(i)

#TODO: dictonary ar keys gula dekhabe than oi tar values gula dekhabe like (['name', 'age', 'department', 'CGPA'], ['Sadrul', 24, 'Computer Science & Engineering', 3.36])
print(student.keys(), student.values())


# TODO: dictonary ar keys ar sathe value ak sathe dekhai like protitar sathe sathei ooitar value dekhai
print(student.items())