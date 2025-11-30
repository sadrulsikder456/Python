# file = open("Ostad/name.txt", "r")
# content = file.read()
# print(content)
# file.close()

with open("Ostad/name.txt", "r") as f:
    content = f.read()
    print(content)

with open("Ostad/name.txt", "a") as f:
    f.write("\nI Love Rabeya")

line= ['\nI Love Coding\n', 'I Love Python\n', 'I Love Bangladesh']

with open("Ostad/name.txt", "a") as f:
    f.writelines(line)