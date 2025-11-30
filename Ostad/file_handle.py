# file = open("Ostad/name.txt", "r")
# content = file.read()
# print(content)
# file.close()

with open("Ostad/name.txt", "r") as f:
    content = f.read()
    print(content)
    
