class employee:
    company_name="Rabeya Ltd"  # Class variable
    def __init__(self,name,salary):
        self.employee_name=name      # Instance variable
        self.employee_salary=salary  # Instance variable
    def display_info(self):          # Instance method
        print(f"Employee Name: {self.employee_name}, Salary: {self.employee_salary}, Company: {employee.company_name}")
    
    @classmethod
    def change_company_name(cls, new_name):  # Class method
        cls.company_name = new_name

ob1= employee("Sadrul", 50000)
ob2= employee("Rabeya", 60000)
ob1.display_info()
employee.change_company_name("New Rabeya Ltd")
print(ob1.company_name)
print(ob2.company_name)