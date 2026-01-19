class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

st1=student("sadrul",23,"A+")
print(st1.get_info())
print(st1.name)