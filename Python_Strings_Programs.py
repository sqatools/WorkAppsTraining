# Program : get all the upper case and lower case words separatelly.

str1 = "Hello MY name is ANKIT and my AGE is 20 and LIVE in Pune"
output1 = ''
output2 = ''
word_list = str1.split(" ")
for word in word_list:
    if word.isupper():
        output1 = output1 + word + " "
    else:
        output2 = output2 + word + " "

print(output1)
print(output2)


# Program : print count of each word
str11 = "Hello my name is ANKIT and my AGE is 20 and name LIVE in Pune NAME ANKIT"
# output = {'Hello' : 1, 'ANKIT': 2 ...}
output = {}
word_list = str11.split(" ")
print(word_list)
for word in word_list:
    w_count = str11.count(word)
    output[word] = w_count
    print(output)

print("Each word count :", output)


#get user name and password from string

str1 = """
agagkajfgja
afgaskjfaskfja
asfaksjfasd   name:username1
ddaffad password:password1
Python is fun to learn I have some cred
fdfsda name:adminuser
Learning is fun
fad password:adminpassword
"""
"""
print("_"*40)
name_output = ''
password_output = ''
word_list = str1.split(" ")
print(word_list)
for word in word_list:
    if 'name' in word and ':' in word:
        name_output = name_output + word + ","
    elif 'password' in word and ":" in word:
        password_output = password_output + word + ","


print(name_output)
print(password_output)
"""

name_output = ""
password_output = ""

lines_list = str1.split("\n")
print(lines_list)

for line in lines_list:
    #print(line)
    word_list = line.split(" ")
    for word in word_list:
        print(word)
        if 'name' in word and ":" in word:
            name_output = name_output + word + " ,"
        elif 'password' in word and ':' in word:
            password_output = password_output + word +" ,"


print(name_output)
print(password_output)

# Get production environment URL from json file
import json

json_file = open("test_data.json", "r")

data = json.load(json_file)
print(data)
print(data['env']['prod']['url'])
print(data['env']['prod']['browser'])



