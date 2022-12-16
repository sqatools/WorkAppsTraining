Dict1 = {'a': 123, 'b' : 456, 'c': 567}

# Add data to dict

Dict1['d'] = 5678
print(Dict1, type(Dict1))
"""
-> Dict only contains unique key
-> Only immutable data type can be key int, float, string, tuple
-> Any type of data can be value in the dict
-> It is mutable data type, we can modify anytime.
"""
Dict1 = {'a': 123, 'b' : 456, 'c': 567, 'd': 678}

# Dict methods
print(dir(dict))

"""
'clear', 'copy', 'fromkeys', 'get', 
'items', 'keys', 'pop', 'popitem', 
'setdefault', 'update', 'values'
"""

# Add data to the dict.

Dict1['e'] = 678

dict2 = {'p' : 345, 'q': 123}

# update : we can update data from one dictionary to another.
Dict1.update(dict2)
print(Dict1)

# Remove data from dictionary
# pop
dictp = {'a': 123, 'b': 456, 'c': 567, 'd': 678, 'e': 678, 'p': 345, 'q': 123}
output = dictp.pop('q')
print(output)
print(dictp)

output2 = {}
output2['q']= output
print(output2)

# popitem
print("_"*50)
dictx = {'a': 123, 'b': 456, 'p': 345, 'c': 567, 'd': 678, 'e': 678, 'list1': [5, 7, 3, 8]}

output3 = dictx.popitem()
print(output3, type(output3))
print("key =", output3[0], "value =", output3[1])
print(dictx)

# Clear : clear all the data from dictionary

dictx.clear()
print("dictx :", dictx)

# Delete from memory
del dictx
#print("dictx :", dictx)

# Get data from dict : get method return the data of any specific key, if key does not
# exist then, it will return default value
dictx = {'a': 123, 'b': 456, 'p': 345, 'c': 567, 'd': 678, 'e': 678, 'list1': [5, 7, 3, 8]}

#print(dictx['f'])

output = dictx.get('d', 'python')
print(output)

# Keys method : This method list of keys

output1 = dictx.keys()
output2 = dictx.values()

print("keys:", output1)
print("values:", output2)

# Items

output_data = dictx.items()
print(output_data)

for key, value in dictx.items():
    print(key, ":", value)


for data in dictx:
    print(data)

# copy method
# Shallow copy
dictp = {'a': 678, 'b': 678, 'c': 233}
dictq = dictp
dictq['d'] = 111

print("dictp:", dictp)
print("dictq:", dictq)

# Deep Copy
print("*"*60)
dictp1 = {'a': 678, 'b': 678, 'c': 233}
dictq1 = dictp1.copy()
dictq1['d'] = 111

print("dictp1:", dictp1)
print("dictq1:", dictq1)


school = {
    'teacher': [
        {'mobile': 45678, 'name': 'tech1', 'email': 'tech1@gmail.com'},
        {'name': 'tech2', 'email': 'tech2@gmail.com', 'mobile': 45665678},
        {'name': 'tech3', 'email': 'tech3@gmail.com', 'mobile': 456756548},
        {'name': 'tech4', 'email': 'tech4@gmail.com', 'mobile': 456565478}
    ],
    'student': [
        {'name': 'stud1', 'email': 'stud1@gmail.com', 'mobile': 4567865999},
        {'name': 'stud1', 'email': 'stud1@gmail.com', 'mobile': 88888888},
        {'name': 'stud2', 'email': 'stud2@gmail.com', 'mobile': 45665678},
        {'name': 'stud3', 'email': 'stud3@gmail.com', 'mobile': 456756548},
        {'name': 'stud4', 'email': 'stud4@gmail.com', 'mobile': 123456789}
    ]
}

student_name = 'stud1'

for key, value in school.items():
    #print(key, ":", value)

    if key == 'student':
        student_data = value
        for data in student_data:
            #print(data)
            st_name = data['name']
            #print(st_name)
            if st_name == student_name:
                print(data['mobile'])
                break
    else:
        continue


# Write a python program to get length of each word as value.
str1 = "Python Programming Language"
dict1 = {"Python" : 6, "Programming" : 11, "Language" : 8}




