my_list=[]
for i in range(5):
    element=int(input(f"Enter the {i+1}th element: "))
    my_list.append(element)
print("The list is:",my_list)
my_list.remove(min(my_list))
print(my_list)
my_list.sort()
print("The sorted list is:",my_list)

