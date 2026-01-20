a=[1,2,3,4,'a',5,6,7,8]

for i in a:
    if type(i) == type('b'):
        break
    else:
        print(i)
 
for i in a:
    if type(i)==type('b'):
        continue
    else:
        print(i)