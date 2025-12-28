class employee:
    company_name = "Tech Solutions"  # Class variable

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_salary(self, password):
        if password == "admin":
            return self._salary
        else:
            return "Unauthorized Access!"

    def set_salary(self, password, salary):
        if password == "admin":
            self._salary = salary
            print(f"Salary Updated : {self._salary}")
        else:
            print("Unauthorized Access!")


emp = employee("John Doe", 50000)
print(emp.get_salary("admin"))
emp.set_salary("admin", 120000)
print(emp.get_salary("user"))  # Unauthorized Access!
print(emp.get_salary("admin"))  # John Doe
