mark=int(input("Enter your mark:"))
if mark>=80:
    print("A+")
elif  mark <= 79 and mark>=70:
    print("A")
elif mark <= 69 and mark>=60:
    print("A-")
elif mark <= 59 and mark>=50:
    print("B")
elif mark<50:
    print("Fail")