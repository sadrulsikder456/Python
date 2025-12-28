class school:
    school_name="Rabeya School"  # Class variable
    @classmethod
    def calculate_grade(cls, marks):
        if marks >= 90:
            return 'A+'
        else:
            return 'F'
sc=school()
print(sc.calculate_grade(75))  
