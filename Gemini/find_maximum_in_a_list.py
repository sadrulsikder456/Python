def find_maximum(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max
my_list=[]
n=int(input("Enter the number of elements of this list:"))
for i in range(n):
    element=int(input(f"Enter element {i+1}:"))
    my_list.append(element)

largest_number=find_maximum(my_list)
print(f"the largest number of this list is: {largest_number}")