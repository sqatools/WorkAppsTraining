str1 = "Good Morning"

print(str1[0])
# Get substring from the string using slicing
# Rule1 : str1[initial index : end index] : it always exclude the end index

output = str1[0:4]  # Good
print(output)

output2 = str1[2:7]  # od Mo
print(output2)

output22 = str1[2:-2]
print("output22 :", output22)

# Rule2 : str[:end_index] : default initial index is zero

output3 = str1[:8]  # Good Mor
print(output3)

output33 = str1[:-1]  # Good Mornin
print("output33:", output33)


# Rule3 : str[initial_index :] : default end index will be len of the string

output4 = str1[2:]
print(output4)  # od Morning

output44 = str1[-1:]  # g
print("output44 :", output44)  # od Morning

# Rule4 : str[initial index: end_index : diff of index value]
print("_"*50)
str2 = "Python Programming"

output = str2[0: 5: 1]
print("output:", output) #

output2 = str2[0: 10: 2]
print("output:", output2) #Pto r

# Default initial index is zero
output3 = str2[:11:3]
print(output3)

# Default end index is end of the string and default initial index

output4 = str2[::1]
print("output4:", output4)

# default initial index is -1 and default end index is -len(str)
output4 = str2[::-2]
print("output4:", output4)

#program
input_str = "Pytgsfdggdsfgdsfgdfsghon"
output = "nythoP"

first_char = input_str[0]
last_char = input_str[-1]
middle_str = input_str[1: -1]

a, b, c = input_str[0]*2,  input_str[-1]*2, input_str[1: -1]
print("a:", a)
print("b:",b)
print("c:",c)

print("output:", last_char+middle_str+first_char)
###################
#string formating

name= "Ankit"
age = 20
city = "Pune"
# str = "Hello my name is Ankit and my age is 20 and live in Pune"

# concatenation with plus operator
output1 = "Hello my name is "+name+" and my age is "+str(age)+" and live in "+city
print(output1)
# format method
output2 = "Hello my name is {} and my age is {} and live in {}".format(name, age, city)
print(output2)

# f string formating
output3 = f"Hello my name is {name} and my age is {age} and live in {city}"
print(output3)

#######################################################
# String Method
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

str2 = "We arE learNing PythoN"
# Index method : can provide index of any character
print("index of l:", str2.index('l'))

# Convert to upper case
print(str2.upper()) # WE ARE LEARNING PYTHON

# Convert to lower cases
print(str2.lower()) # we are learning python

# Title case conversion
print(str2.title()) # We Are Learning Python

# Swap the cases from upper to lower and lower to upper
print(str2.swapcase()) # wE ARe LEARnING pYTHOn

str11 = "HELLO"
# check given string in the upper not
print("is upper :", str11.isupper())

print("is lower :", str11.islower())

# Split method

str22 = "Python learning is fun"
str33 = "Python,learning,is,fun"
output22=  str22.split(" ")
output33 = str33.split("l")

print("output22:",str22, output22)
print("output33:",str33, output33)

# for v in str22:
#     print(v)
#
for w in output33:
    print(w)

# write program to get longest word in the string
print("_"*50)
str1= "Python learning fgdgdsgdfggdfgfg is fun"
long_len = 0
long_word = ''
word_list = str1.split(" ")
for word in word_list: # word = Python, learning, is, fun
    word_len = len(word) # len = 6, 8, 16, 2, 3
    if word_len > long_len: # 6 > 0, 8 > 6, 16> 8, 2> 16, 3> 16
        long_len = word_len  # 6, 8, 16
        long_word = word   # Python, learning, fgdgdsgdfggdfgfg
    else:
        continue

print(long_word)
print(long_len)

# Get count of any character in the given string
print("_"*50)
str33 = "Python learning fgdgdsgdfggdfgfg is fun"
print(str33.count('g'))

# Replace any substring from given string
output = str33.replace('Python', 'Java')
print(output)

output2 = str33.replace('Py', 'Java').replace('Java', 'Py').replace("is", "are"). replace(" ", ",")
print(output2)

# Remove preceding and trailing spaces from given string
print("_"*50)
str4= "     Learning Programming     "
print(str4)

output3 = str4.strip()
print(output3)

# Remove left side space
output4 = str4.lstrip()
print(output4)

# Remove right side space
output5 = str4.rstrip()
print(output5)

# find method: if given substring is available , then find method return index of the substring
# and if substring does not exist , then it will return -1
print("_"*50)
input_str = "Remove preceding and trailing spaces from given string"
output7 = input_str.find('ande')
print(output7)

output = True if 'andre' in input_str else False
print(output)

# join method :
str9 = "Python   "
output9= "&*@#*".join(str9) # P*y*t*h*o*n
print(output9)

#

str10 = "2345"
print(str10.isnumeric())

input_str = """
Remove preceding 5656546356 and trailing spaces 3653564326 from given string
Remove 3432 preceding and 2543422344 trailing spaces from 45543 given string
"""
for word in input_str.split(" "):
    if word.isnumeric() and len(word) >= 10:
        print(word)
    else:
        continue



#






