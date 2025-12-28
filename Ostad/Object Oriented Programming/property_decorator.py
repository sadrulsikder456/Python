class employee:
    company_name = "Tech Solutions"  # Class variable

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


ob1 = employee("John Doe", 50000)
print(ob1.salary)
ob1.salary = 120000
print(ob1.salary)
