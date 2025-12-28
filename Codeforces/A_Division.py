test=int(input())
for _ in range(test):
    division=int(input())
    if(division<=1399):
        print("Division 4")
    elif (division>=1400 and division<=1599) :
        print("Division 3")
    elif(division>=1600 and division<=1899):
        print("Division 2")
    elif(division>=1900):
        print("Division 1")