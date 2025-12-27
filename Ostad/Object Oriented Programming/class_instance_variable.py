class school:
    school_name="Rabeya School"  # Class variable
    def __init__(self, name):
        self.student_name=name

sc1=school("Sadrul")
sc2=school("Rabeya")
print(sc1.school_name, sc1.student_name)  # Instance variable
print(sc2.school_name, sc2.student_name)  # Instance variable