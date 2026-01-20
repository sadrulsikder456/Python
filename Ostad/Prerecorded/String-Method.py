a="this is python"
print(a.title()) #This Is Python
print(a.upper()) #THIS IS PYTHON    
print(a.lower()) #this is python
print(a.capitalize()) #This is python
print(a.count('is')) #2
print(a.find('is')) #2
print(a.replace('is','was')) #thwas was python
print(a.split()) #['this', 'is', 'python']
print(a.startswith('this')) #True
print(a.endswith('java')) #False
print(a.index('p')) #8
print(a.isalpha()) #False
print(a.isdigit()) #False
print(a.islower()) #True
print(a.isspace()) #False
print(a.istitle()) #False
print(a.swapcase()) #THIS IS PYTHON
print(a.zfill(20)) #0000000this is python
print(a.center(30)) #        this is python
print(a.ljust(30)) #this is python
print(a.rjust(30)) #        this is python
print(a.strip()) #this is python
print(a.partition('is')) #('th', 'is', ' is python')
print(a.rpartition('is')) #('this ', 'is', ' python')
print(a.encode()) #b'this is python'
print(a.format()) #this is python
print(a.format_map({'a':'this','b':'is','c':'python'})) #this is python
print(a.removeprefix('this')) # is python
print(a.removesuffix('python')) #this is
print(a.translate(str.maketrans('this','THIS'))) #THIS IS pyton
print(a.count('is',0,10)) #2
print(a.find('is',0,10)) #2
print(a.index('is',0,10)) #2

