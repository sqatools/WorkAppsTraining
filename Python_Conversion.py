"""
Python Data Type
1. Numbers:
    i. Int
    ii. Float

2. Sequentials:
    i. String
    ii. List
    iii. Tuple

3. Dictionary
4. Sets
5. Boolean
"""

# int
num1 = 456
# int -> float
output = float(num1)
print(output, type(output))

# int ->  string
output2 = str(num1)
print(output2, type(output2), output2[0])

# int -> list # 'int' object is not iterable
#print(list(num1))
# int -> tuple # 'int' object is not iterable
# int -> dict : not possible
# int -> set : not possible
# num2 = 5678
# print(set(num2))

####### float ##########
num11 = 5.67
# float ->  int
print(int(num11))  # 5
# float -> string
output3 = str(num11)
print(output3, type(output3), output3[2])

######### string ##########

str1 ='Hello'
# str -> int

#print(int(str1)) # invalid literal for int() with base 10: 'Hello'
# If string has char then str ->  int conversion is not possible

str11 = '5683'
output = int(str11)
print(output, type(output), output*2)

# str -> float
str12 = '56.83'
output12 = float(str12)
print(output12, type(output12), output12*3)

# str -> list
str4 = "Python"
list_output = list(str4)
print(list_output, type(list_output))  # ['P', 'y', 't', 'h', 'o', 'n']

# str -> tuple
tup_output = tuple(str4)
print(tup_output, type(tup_output))  # ('P', 'y', 't', 'h', 'o', 'n')

# str -> dict  # dictionary update sequence element #0 has length 1; 2 is required
#str5 = "Programming"
#print(dict(str5))

import json
str6 = '{"a": 345, "b": 123, "c": 567}'
#print(dict(str6))
output6 = json.loads(str6)
print(output6, type(output6), output6['c'])

# str -> set
str7 = "Hello"
print(set(str7))  # {'H', 'l', 'e', 'o'}

################## list #######################
list1 = [5, 7, 8, 1]

# list -> str
output = str(list1)
print(output, type(output),  output[0])

# list -> tuple
output2 = tuple(list1)
print(output2, type(output2), output2[2])

# list -> dict : not possible
#output3 = dict(list1)
#print(output3)

# list -> set

list11 = [4, 6, 2, 8, 2, 4, 5, 6]

output3 = set(list11)
print(output3, type(output3))
print(list(output3))

################# Tuple #############
tup = (4, 7, 2, 8)
# tuple -> str
output1 = str(tup)
print(output1, type(output))
# tuple -list
output2 = list(tup)
print(output2, type(output2))


############# Dictionary ######
dict1 = {'a': 123, 'b': 345}
#dict1 -> int : not possible
# dict -> float : not possible
# dict -> string

output1 = str(dict1)
print(output1, type(output1), output1[0], output1[4])
# dict -> list
output2 = list(dict1)
print("list output :", output2)
# dict -> tuple
output3 = tuple(dict1)
print("tuple output :", output3)
# dict -> set : not possible

######### Set ################

set1 = {5, 7, 2, 8, 12}
# set -> int
# set -> float
# set -> string
output11 = str(set1)
print(output11, output11[1], type(output11))

# set -> list
output_list = list(set1)
print(output_list, output_list[2], type(output_list))  # 7

# Set -> tuple
output_tup = tuple(set1)
print(output_tup, output_tup[2], type(output_tup)) # 7

# Set -> Dict : not possible









