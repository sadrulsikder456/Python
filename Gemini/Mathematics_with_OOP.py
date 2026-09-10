class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        area=3.1414*self.radius**2
        print(f"The area is :{area}")
    def get_circumference(self):
        poridhi=2*3.1416*self.radius
        print(f"The poridhi is: {poridhi}")

circle1=Circle(3)
circle1.get_area()
circle1.get_circumference()