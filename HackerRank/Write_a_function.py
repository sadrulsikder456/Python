year=int(input())
s=False
if (year%4==0 and year%100!=0) or (year%400==0):
    s=True
print(s)