from glob import translate

# Capitaslizve (capitalize the first index)
hello = "heLLo, World!"
print(hello.capitalize())
hello1='hello world'
hello.capitalize()
hello_2='@hello world'
hello_2.capitalize()
hello_3="-hello world"
hello_3.capitalize()

#casefold( It converts a string to lowercase)
y='WELCOME TO INDIA'
y.casefold()
print(y.casefold())
x='python'
x.casefold()
y='1234WeLcOmE To InDiA'
y.casefold()

#center( used to align text within a given string length)
x='python'
print(x.center(10,"$"))
y='hello python'
y.center(19,'&')
x='python'
x.center(10,'*')
x.center(10)

#count( used to count the number of occurrences of a particular element)
y=('It was a cold, cold day')
print(y.count('cold',2,12))
print(y.count('c',2,16))

x='hi python.hi string'
print(x.count('hi'))

x='hi python.hi string'
x.count(' ')

#find(find the index of the first occurrence of a substring from the given string)
# if the substring is not found then it return -1
x='hi python.hi string'
print(x.find('hx'))
y='welcome to python'
y.find('to',2,7)

# encode ( convert a string into bytes using a specified encoding format )
name3="Ståle"
name3.encode(encoding="ascii",errors='ignore')

# rfind(to return the highest index value of the last occurrence of the substring from the input string)
x='python'
print(x.rfind('o'))
y='hi python, hello python'
y.rfind('python')
y.rfind('y')




# endswith(to check if a string ends with a specified suffix)
y='hi python.hi string'
print(y.endswith('string'))
print(y.startswith('python',3,10))

# startswith( determines whether a string begins with a specified substring)
x='hi python.hi string'
print(x.startswith('hi'))

# expandtabs(used to replace all occurrences of tab characters (\t) in a string with a specified number of spaces)
x='p\ty\tt\th\to\tn'
print(x.expandtabs(2)) #this 2 indicates how many space that  tab contains
print(x.expandtabs(4))

# index( finding the index of a specific element in a sequence)
# if the substring is not found then it return- error
x='this y is an python world'
print(x.index('i'))

# rindex(finds the last occurrence of the specified value)
x='python'
print(x.rindex('o'))

#isalnum(utilized to verify if all the characters within a string are either numbers (0-9) or letters (a-z or A-Z))
x='jamesbond007'
print(x.isalnum())

# isalpha(to check if the passed character is an alphabet or not)
x='dhoni7'
print(x.isalpha())

 # isdecimal( built-in method that is used to check whether a given string is a decimal or not)
x='0.007'
print(x.isdecimal())

 # isdigit(returns a Boolean value TRUE if all the values in the input string are digits; else it returns FALSE)
x='\u00BD'
print(x.isdigit())

#isidentifier(used to check and return value TRUE
# if the input string is a valid identifier else return value FALSE)
x='python007'
print(x.isidentifier())

# islower(returns True if all the characters are in lower case, otherwise False)
x='my name is python'
print(x.islower())

# isnumeric(checks if the string contains any numeric value or not)
x='123452'
s4 = "i"
print(x.isnumeric())
print(s4.isnumeric())

#isprintable (returns “True” if all characters in the string are printable or the string is empty,
# Otherwise, It returns “False”)
x='python'
print(x.isprintable())

# isspace(returns True if all the characters in a string are whitespaces, otherwise False.)
x='  '
print(x.isspace())
x=x.strip()
print(x.isspace())

#istitle(returns True if all words in a text start with  upper case letter,
# AND the rest of the word are lower case letters, otherwise False)
x='Vishal'
print(x.istitle())

#isupper(if a character is an uppercase letter.)
x='vishal'
print(x.upper())

# islower(if a character is an lowercase letter.)
x='VISHAL'
print(x.lower())

# join(takes all items in an iterable and joins them into one string)
x="vishal,shanjay"
y='*'
print(y.join(x))

# ljust(returns a left-justified string according to the width specified and fills
# the remaining spaces with blank spaces if the character argument is not passed)
x='python'
print(x.ljust(10,'$'))

# rjust(returns a right-justified string according to the width specified and
# fills the remaining spaces with blank spaces if the character argument is not passed)
x='python'
print(x.rjust(10,'$'))

# lstrip( removes the whitespace at the beginning of a string)
x='%%%%python world%%%%%'
print(x.lstrip('%'))

# rstrip(removes the whitespace at the ending of a string)
x='%%%%python world%%%%'
print(x.rstrip('%'))

# partition(specified string, and splits the string into a tuple containing three elements)
x='hello,,welcometo india'
print(x.partition(','))
tuple1=x.partition(',')

# rpartition(searches for the last occurrence of a specified string, and
# splits the string into a tuple containing three elements)
x='hello welcome to india'
print(x.rpartition(','))

# removeprefix(removes the prefix and returns the rest of the string)
x='python'
print(x.removeprefix('yt'))

# removesuffix(Remove a suffix from an object series)
x='python'
print(x.removesuffix('hon'))

# replace(replaces a specified phrase with another specified phrase)
x='hello python world'
print(x.replace('python','vishal'))

# split(splits a string into substrings based on a delimiter and returns a list of these substrings)
x='india.america.russia'
print(x.split(','))
print(x.split('.'))

# rsplit(method that splits a string into a list of substrings from the
# right end of the string based on a specified delimiter)
x='bread,bun,jam'
print(x.rsplit(',',1))

# splitlines( built-in string method in Python that is used to split a multi-line string into a list of lines)
print("Nirmal and \nvishal are friends")
name2="Nirmal and \nvishal are friends \n his brother also"
name2.splitlines()
# swapcase
name3="nIrmaL"
name3.swapcase()

# title
name5="hello nirmal picture"
name5.title()

# zfill(adds zeros (0) at the beginning of the string, until it reaches the specified length)
name4="Nirmal"
name4.zfill(10)

name4="-vishal"
name4.zfill(8)

# format(format specifiers, that are used to insert values )

name5="nirmal {} picture"
name5.format("took a")

name5="nirmal {value1} picture {value2} camera"
name5.format(value2="took a",value1="with")

name5="nirmal {1} picture {0} camera"
name5.format("took a","with")

name6="ragu is ragu and ragu nath"
print(name6.strip(""and",1,10"))


# pending Maketrans,translate,formatmap
# dir(str)

# format_map (
x={"name":"Nirmal","age":90}

print("hello {name},your age is {age}".format_map(x))
# translate()

name_1="vishal"
mydict={97:"S"}
name_1.translate(mydict)

chan={"s":"S","a":"A"}

table=name_1.maketrans(chan)
name_1.etranslate(table)