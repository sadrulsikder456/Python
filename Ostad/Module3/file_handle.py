f = open("Ostad/Module3/file.txt", "a")
f.write("I love you Rabeya")
f.close()

with open("Ostad/Module3/file.txt", "r") as f:
    content = f.read()
    print(content)