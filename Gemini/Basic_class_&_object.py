class Student :
    def __init__ (self,name,student_id):
        self.name= name
        self.id= student_id
    def display_info(self):
        print(f" The student name is {self.name} & the id is {self.id}")
student1=Student("Sadrul",1322)
student1.display_info()