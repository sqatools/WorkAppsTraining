"""
r : read mode
w : write mode
a : append mode
"""
"""

file = open('read_data.txt', 'r')
#data = file.read()

#data10 = file.read(10)
#print(data10)

# read single
#data_line = file.readline()
#print(data_line)

"""
# read 5 lines from file
"""
for i in range(5):
    print(file.readline(), end="")
"""
# get all the line list
"""
line_list = file.readlines()
print(line_list)

print(line_list[-2:])
"""
"""
# Get all the email ids from the file.
email_list = []
file = open('read_data.txt', 'r')
file_lines = file.readlines()

for line in file_lines:
    word_list = line.split(" ")
    #print(line, word_list)
    for word in word_list:
        if '@' in word:
            email_list.append(word)
        else:
            continue

print(email_list)
file.close()
"""
#### Context Manager  ######
# write mode overwrite the existing content of the file.
"""
str2= "This is new line to be added"
with open("write_data.txt", "w") as file:
    file.write(str2)
"""

# open file with append mode and add content to the file
"""
str2= "\nThis is new line to be added with append mode"
with open("write_data.txt", "a") as file:
    file.write(str2)

"""

# Read json file:
import json
with open("test_data.json", "r") as file:
    #data = file.read()
    dict_data = json.load(file)
    print(dict_data, type(dict_data))

    print("Browser:", dict_data['browser'])
    print("URL:", dict_data['url'])


