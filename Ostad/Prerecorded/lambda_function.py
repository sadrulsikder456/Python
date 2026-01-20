from functools import reduce
square = lambda x: x*x
print (square(500))
add = lambda a,b : a+b
print (add(200,300)) 
students = [('rahim', 60),('karim', 70),('salim', 50)]
sorted_student= sorted(students,key =lambda x: x[1])
print (sorted_student)

#map(), filter(), reduce()

#map
nums=[1,2,3,4]
sq_nums= list(map(lambda x: x*x,nums))
print(sq_nums)
#filter
even_nums= list(filter(lambda x: x%2==0,nums))
print(even_nums)
#reduce
sum_nums= reduce (lambda a,b: a+b, nums)
print(sum_nums)