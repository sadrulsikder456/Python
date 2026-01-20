a={ 'rahim':25, 'karim':30, 'jamal':22 ,1:[1,2,3,4,],2: [1,2,] }

print(a)

for i in a:
    print(i)

for i in a.values():
    print(i)

print(a.keys(), a.values())

for k,v in a.items():
    print(f'key: {k}  value: {v}')

a=[1,2,3]
b=["Mango", "Banana", "Orange" ]

print(dict(zip(a,b)))