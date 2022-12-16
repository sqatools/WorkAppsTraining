# range(initial, last value, difference)
"""
for i in range(1, 40, 1)
    print(i)
"""

# for i in range(1, 11, 1):
#     print(i)

# default initial value is 0 and last value is 1
# for i in range(11):
#     print(i)

# default last value is 1
"""
for i in range(1, 11, 2):
    print(i)
"""
# Print table of given
# num1 = 5
# for i in range(1, 11):
#     print(i, "*", num1, ":", i*num1)


# print number in negative order
"""
for i in range(10, 0, -1):
    print(i, end="-")
"""
"""
# print all the even number from 1 to 30
for i in range(1, 30):
    if i%2 != 0:
        print(i)
"""
# Factorial of any given number
"""
num2 = 6 # 5*4*3*2*1
fact = 1
for i in range(num2, 0, -1):
    fact = fact*i
    print(fact)

print("Factorial of number:", fact)
"""
##### Apply loop on string ####

str1 = "Good Moreninga"

# for char in str1:
#     print(char)

# write a program to get count of vowel
vowels = 'aeiou'
count = 0
for char in str1:
    if char in vowels:
        count += 1
    else:
        continue

print("Vowels count :", count)

##### Apply on list ###########
# Get all odd numbers from the given list
print("_"*50)
print()
list1 = [5, 6, 2, 8, 1, 11]

for var in list1:
    if var%2 != 0:
        print(var, end=" ")

##### apply loop on tuple data #####
print("_"*50)
print()
# Get all the numbers which are divide by 2 or 3
tup1= (4, 6, 2, 7, 8, 11)

for var in tup1:
    if var%2 ==0 or var%3 == 0:
        print(var)

print("_"*50)
len_tup = len(tup1)

print("total length :", len_tup)
for i in range(len_tup):
    #print(i,  tup1[i])
    if tup1[i]%2 == 0 or tup1[i]%3 == 0:
        print(tup1[i])


######### Apply loop on the dict ############
dict1 = {'a': 345, 'b': [4, 6, 8], 'c': (5, 7, 8)}

for key, value in dict1.items():
    print(key,":", value)

for value in dict1:
    print(value)

for value in dict1.items():
    print(value)

##########  Applu loop on set #######
print("_"*40)
set1 = {4, 6, 8, 2, 9, 4}

for data in set1:
    print(data, data**2)

#####################Nested Loop Condition####################
print("_"*40)
"""
for condition:
    code
    for condition2:
        code
"""

# for address in range(4):
#     for pkg in range(3):
#         print("address :", address, "pkg :", pkg)
#     print()
#

for address in range(4):
    print("Address :", address)
    for pkg in range(3):
        print("Pak:", pkg)
        for item in range(3):
            print("item:", item)
    print()

# program to check given number is prime number or not
"""
-> take any number num=20
-> consider that number is prime = True
-> apply loop from 2 to 19 to divide the number for i in range(2, num)
-> then check given number is divide by any of the numbers from 2 to 9 
    if num% == 0:
        prime = False
        break
-> if still prime == True then we can say it is prime
"""
"""
num=23
prime = True
for i in range(2, num):
    if num%i == 0:
        prime = False
        break
    else:
        continue

if prime:
    print("Given number is prime number:", num)
else:
    print("Given number is not prime number:", num)
"""
# Get all the prime number from 1 to 100

for num in range(1, 100):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        else:
            continue

    if prime:
        print(num, end=" ")
    else:
        continue


######## Break and continue ############
print("_"*30)
for i in range(10):
    # print("initial:", i)
    # continue
    if i == 3 or i == 4:
        continue
    elif i == 7:
        break
    print("end=:", i)

################# While Loop ######
print("_"*40)
num = 0
while num <= 10:
    print(num)
    num += 1

count = 10
while True:
    print("Hello:", count)
    if count == 1:
        break
    else:
        #count += 1
        #count = count + 1
        count -= 1