a=[1,10,20,33,24,34,55]

# normal way 
result=[]
for i in a:
    if i%2==0:
        result.append(i)
print(result)

# using list comprehension
new_result = [i for i in a if i%2==0]
print(new_result)