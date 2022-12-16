"""
Python Data Type
1. Numbers:
    i. Int  : num = 123
    ii. Float : num = 345.67

2. Sequentials:
    i. String : str1 = 'Hello'
    ii. List : list1 = [4, 7, 9, 2, 6, 'Python']
    iii. Tuple : Tup1 = (4, 7, 2, 'a', 'Programming')

3. Dictionary :
keys : int, float, string, tuple
values : int, float, string, list, tuple, dict, set
dict1 = {'a' : 123, 456: 'Python', 2.5 : (4, 7, 8), (4, 5) : {'name': 'Rahul', 'age': 56}}

4. Sets :
member data : int, float, string, tuple
set1 = {4, 5, 'a', (5, 7, 8), 3.5}

5. Boolean : True and False
"""

# Integer
num1 = 5
num2 = 65674576675
num3 = 546347645367575678657
num4 = 0
print(num1, type(num1))
print(num2, type(num2))
print(num3, type(num3))
print(num4, type(num4))

# Float
var1 = 50.5
var2 = 23.789967657567657456
var3 = 542352454543543.2
print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))

################### list #########################
"""
-> List is mutable data type, that change at any point of time
-> List follows positive and negative indexing for all the the data.
-> We can store any type of data in the list. e.g int, float, tuple , dict, set
-> We generally use list where data is data is regullarly e,g
   institude registration
   Weather information
   data base related operation
"""
print("_"*30)
#        0  1     2        3
list1 = [2, 3.5, 'Python', [3, 5, 6]]
#        -4  -3   -2       -1

print(list1, type(list1))

data = list1[0]  # positive index
print(data, type(data))

data1 = list1[-4]  # Negative Index
print(data1, type(data))

sub_list = list1[-1]
print(sub_list, type(sub_list))
print(sub_list[1], type(sub_list[1]))
print(list1[-1][1])

# Methods of list
print(dir(list))

# 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

###################### Tuple #######################
"""
-> Tuple follow same positive and negative indexing like list
-> Tuple is immutable datatype, once it is define we can not change it.
-> We can store anytype of data in the tuple e.g. int, float, list, tuple, dict, set
-> Generally we use tuple where we dont want to changes the data in the future
   that is going to remain fixed. e.g days in week, months in year.
"""

#      0   1  2  3  4     5         6
Tup1 = (5, 7, 3, 8, 2.5, (5, 7, 3), [2, 6, 8])
#      -7 -6 -5 -4 -3     -2        -1
print(type(Tup1), Tup1)

print(Tup1[2])  # 3
print(Tup1[-2])  # 8

print(Tup1[5][1])  # 7

print(Tup1[-1][2])  # 8


################ String ########################

str1 = 'Python'
str2 = "Programming"
str3 = '''Good Morning'''
str4 = """Hello
How are you"""

print(str1,  type(str1))
print(str2,  type(str2))
print(str3,  type(str3))
print(str4,  type(str4))

#            0 1 2 3 4
#input_str = "H e l l o"
#           -5-4-3-2-1
input1 = "Hello"
print(input1[0])  # H

print(input1[-1])  # O

str1 = "Python"
str2 = "Programming"
output = str1 +" "+ str2

print(str1 +" "+ str2)
print(output)

#############  Dictionary data type ###########

dict1 = {'a' : 345, 'b': 567, 'c': 457, 'a': 123, 34: "Python"}

print(dict1['a'])
"""
-> dict is mutable data type, we can modify any point of time
-> dict only accept unique key.  duplicate key is not allowed
-> All immutable data type can be key in the dictionary e,g. int, float, tuple, string
-> Any type of data can be value in the dict, int, float, string, tuple, list, dict.
->  Dict is unstructure data type, it does not follow any indexing
"""
"""
dict1[(5, 7, 8)] = [6, 8, 2, 9]

print(dict1)
dict1[567] = {'name': 'Rahul', 'age': 34}
print(dict1)

print(dict1[(5, 7, 8)])

dict2 = {('math', 'phy', 'chem') : [['mtech1', 'mtech2'], ['ptech1', 'ptech2'], ['ctech1', 'ctech2']]}

print(dict2[('math', 'phy', 'chem')])

keys = dict2.keys()
values = dict2.values()
print("keys:", keys)
print("Values:", values)

print(keys, type(keys))
print(values, type(keys))


school = {
    'teacher': [
        {'mobile': 45678, 'name': 'tech1', 'email': 'tech1@gmail.com'},
        {'name': 'tech2', 'email': 'tech2@gmail.com', 'mobile': 45665678},
        {'name': 'tech3', 'email': 'tech3@gmail.com', 'mobile': 456756548},
        {'name': 'tech4', 'email': 'tech4@gmail.com', 'mobile': 456565478}
    ],
    'student': [
        {'name': 'stud1', 'email': 'stud1@gmail.com', 'mobile': 456786546},
        {'name': 'stud2', 'email': 'stud2@gmail.com', 'mobile': 45665678},
        {'name': 'stud3', 'email': 'stud3@gmail.com', 'mobile': 456756548},
        {'name': 'stud4', 'email': 'stud4@gmail.com', 'mobile': 456565478}
    ]

}
print("_"*30)
for key, value in school.items():
    if key == 'teacher':
        #print(school[key])
        for data in school[key]:
            print(data['mobile'])
    else:
        continue

"""
######################### Sets ######################
# Set data type store only unique value duplicate data in now allowed
"""
-> set is mutable data type
-> set only contains only unique data , duplicate values are not allowed
-> All the immutable data type can be member of the set, int, float, string, tuple
-> It does not follow any indexing.
-> list and dict can not add the set member.
"""
sets = {5, 'a', 2.6, (2, 6, 7), 5, 'a', 123, '123', 123.5}
print(sets)


