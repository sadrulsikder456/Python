#TODO: ai khane frequency akta dictonary neya hoyeche jei khane user ar theke neya word or sebtance ar charector ar count kore rakha hoyeche

frequency={}
word=str(input("Enter your word or sentence:"))

#TODO: user ar deya word or sentance ar opor loop caliye proti index a j character ache oita frequency dictonary te count kore rakha hocche

for char in word:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print(f"Character frequency : {frequency}")