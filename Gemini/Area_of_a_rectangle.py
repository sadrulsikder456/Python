def calculate_area(length, width):
    area=length*width
    return area

length=float(input("Entr the length of the rectangle:"))
width=float(input("Enter the width off the rectangle:"))
area=calculate_area(length,width)
print(f"The area of this rectangle is: {area}")