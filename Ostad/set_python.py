# {}
# Unordered --> indexing kore access kora jay na
# immutable --> modify kora jay na
# no duplicates

a=[1,2,2,3,4,4,4,5]
s=set(a)
print(s)

b={1,2,3,4,5}
c={4,5,6,7,8}
# union
d=b.union(c)
print(d)
# intersection
e=b.intersection(c)
print(e)
# difference
f=b.difference(c)
print(f)
# symmetric difference  
g=b.symmetric_difference(c)
print(g)