"""
var1 = 'Python'

print(var1, type(var1))

print(id(var1))

var2 = 'Python2'
print(id(var2))
"""

# Delete variable from the memory
#del var2
#print(var2)

# var 1 = 50 : wrong
#var_1 = 60 # right
#1_var = 70 # wrong
# var_2_data = 60 # Right
# __data = 'Programming' # Right
# _var_ = 'Python' # Right
# __var_data = 40  # Right
# _var_4_var2 = 50  # Right

# assign same value to multiple variables
num1 = num2 = 60
print(num1, num2)

# assign different values to diff var at a time.
x, y, z = 60, 70, 80
print(x, y, z)

"""
= : assignment operator
== : equal to oper
!= : not equal to oper
+ : plus oper
- : subtraction
* : multiplication
/ : divide provide output in float 
// :  divide oper, provide output in int.
% : remainder oper.
**(n) : n number of time multiply the values
"""

"""
# compare two var
varx = 50
#vary = 70
vary = 50

print(varx == vary)  # False

# math operations
print("addition:", varx+vary)
print("multiply :", varx*vary)
print("subtract:", varx - vary)

# Divide
num1 = 50
num2 = 6
# divide with single /
output = num1 / num2
print("output:", output, type(output))

print("_"*50)
# divide with double //
output2 = num1 // num2
print("output2:", output2, type(output2))


# Remainder operator %
print("_"*50)
p = 11
q = 2
print("remainder :", p%q)

num11 = 13
print("check even or odd:", num11%2 == 0)

num2 = 3
print("square of number:", num2**2)
print("cube of number:", num2**3)

print("Hello"*5)
"""

# solve math equation
a = 4
b = 5
# a2 -b2 = (a-b)(a+b)
lhs = a**2 -b**2
rhs = (a-b)*(a+b)
print(lhs, rhs)

a = 4
b = 5
c = 6
# a2 = b2 + c2
lhs = a**2
rhs = b**2 + c**2
print(lhs, rhs)

# Get percentage of anu given number
num1 = 550
per = 15

percentage = num1*(per/100)
var = percentage//2
print("15 percent of 550:", percentage)
print("New output:", var)

# input: take input from user, by default input method takes argument as string, we have
# convert it as per our requirements.
num1 = int(input("Please enter your number1:"))
num2 = int(input("Please enter your number2:"))

print("addition :", num1+num2)


