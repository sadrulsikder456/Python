def is_palindrome(string):
    string=string.lower()
    return string==string[::-1]

word=str(input("Enter a word:"))

# this a also a tecnical way to check polindrome 

if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

#TODO: aita khane word ta function a diye boolian result niye oita if,else a diye check kore than print kora hocche.

result=is_palindrome(word)
if result==True:
    print(f"{word} is a polindrome")
else:
    print(f"{word} is not a polindrome")