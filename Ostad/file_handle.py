import os
import pathlib
file = open("Ostad/name.txt", "r")
content = file.read()
print(content)
file.close()

with open("Ostad/name.txt", "r") as f:
    content = f.read()
    print(content)

with open("Ostad/name.txt", "a") as f:
    f.write("\nI Love Rabeya")

line= ['\nI Love Coding\n', 'I Love Python\n', 'I Love Bangladesh']

with open("Ostad/name.txt", "a") as f:
    f.writelines(line)

if os.path.exists('Ostad/name.txt'):
    print("File exists")
else :
    print("File does not exist")

file_path =pathlib.Path('Ostad/name.txt')
if file_path.exists():
    print("File exists")
print(os.path.abspath('Ostad/name.txt'))
print(os.path.getsize('Ostad/name.txt'))