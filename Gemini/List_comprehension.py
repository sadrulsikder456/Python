# list = []

# # for i in range(11):
# #     element = i
# #     list.append(element)

# # for i in list:
# #     if list[i] % 2 == 0:
# #         list[i] = list[i] * list[i]
# #     else:
# #         list.remove(list[i])
# # print(list)


list= [x**2 for x in range(1,11) if x%2==0]

print(list)