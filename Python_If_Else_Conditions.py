"""
if condition:
    code
else:
    code
"""
num1 = 11

print(num1%2 == 0)
if num1%2 == 0:
    print("This is even number")
else:
    print("This is odd number")


"""
Logical Operator 
> : greater than 
< : less than
>= : greater than equal to
<= : less than equal to 
!= : not equal to
== : equal to

or & and
"""

a = 20
b = 20

if a >= b :
    print("a has greater value")
else:
    print("b has greater value")

"""
elif condition

if codition1:
    code
elif condition2:
    code
elif condition3:
    code
else:
    code

"""

p = 500
q = 500

if p > q:
    print("p has greater value :", p)
elif q > p:
    print("q has greater value :", q)
elif p == q:
    print("p and q has same value ", p, q)
else:
    print("No output")

# or : Anyone can be true
# and : both the condition should be true
"""
or
True or False : True
False or True : True
False or False : False
True or True : True

and
True and False : False
False and True : False
False and False : False
True and True : True
"""

"""
num= 25

# check given number is divide by 3 and 5
if num%3 == 0 and num%5 == 0:
    print("This number can be divide by 3 and 5 both :",  num)
else:
    print("We can not divide this num by 3 and 5 :", num)
"""
"""
print("_"*30)
num = 26
# check given number is divide by 3 or 5
if num%3 == 0 or num%5 == 0:
    print("This number can be divide by 3 or 5 both :",  num)
else:
    print("We can not divide this num by 3 or 5 :", num)


print("_"*50)
marks = int(input("Please enter student marks:"))

if marks > 40 and marks <= 50:
    print("Student passed with third grad")
elif marks > 50 and marks <=60:
    print("Student passed with second grad")
elif marks > 60 and marks <=80:
    print("Student passed with first grad")
elif marks > 80 and marks <=100:
    print("Student passed with excellent grad")
elif marks <=40:
    print("You are failed :")
else:
    print("Numbers can not be more than 100")

"""
# Nested If condition
"""
if condition:
    code
    if condition2
        code
    else:
        code
else:
    code
"""
print("_"*50)
round1 = "pass"
round2 = "waiting"
round3 = "Pass"

if round1 == "pass":
    print("Congrats first round is cleared")
    if round2 == "Pass":
        print("Congrats second round is cleared")
        if round3 == "Pass":
            print("Congrats third round is cleared, please receive offer")
        else:
            print("Sorry, third round is not cleared, try next time")
    elif round2 == 'waiting':
        print("You are on hold, please wait for few days for feedback of round2")
    else:
        print("Sorry, second round is not cleared, try next time")
elif round1 == 'waiting':
    print("You are on hold, please wait for few days for feedback of round1")
else:
    print("Sorry, first round is not cleared try next time")


num1 = 51
output = "even" if num1%2== 0 else "odd"
print(num1, output)