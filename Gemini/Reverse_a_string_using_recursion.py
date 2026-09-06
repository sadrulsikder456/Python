def reverse(string):
    if len(string)==0 or len(string)==1:
        return string
    return string[-1]+reverse(string[:-1])

word=str(input("Enter a word:"))
result=reverse(word)
print(f"The reverse of the word {word} is: {result}") 
    