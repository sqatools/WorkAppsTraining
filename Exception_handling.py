
"""
num1 = 40
num2 = 'Hello'

#print("addition :", num1 + num2)

try:
    print("addition :", num1//0)

except Exception as e:
    #print(e)
    print("Addition of string and int is not allowed")
    raise
"""

"""

# try - except - else # Else condition only executes when there is no exception in the program


num1 = 50
num2 = 51
num3 = 70
num4 = 60

try :
    assert num1 != num2
    assert num2 == num3
    assert num3 > num4
    assert num1 != num4
except Exception as e:
    print("Assertion error , numbers did not match")
    raise

else:
    print("Both the numbers are matched")


# write a program to check which are the numbers can divide by 3

"""
"""

try:
    for i in range(1, 30):
        assert i%3 == 0
except:
    print("the number can not divide by 3 :", i)

"""

#### nested exception
"""
try :
     code1
     try:
        code2
    except:
        print("exception1")
except:
    print("exception1")


"""

"""
max_try = 30

try:
    for i in range(1, 1000):
        assert i < max_try
        try:
            print(i)
            assert i%3 == 0
            print("Number successfully divide", i)
        except:
            print("the number can not divide by 3 :", i)
except:
    print("Max try excceded :",max_try, i)
    raise 

"""

"""
# try -> except -> finally : finally block always executes even there is exception in the programs.


try:
    for i in range(30):
        if i%2 == 0:
            print(i)
            assert i < 50
        else:
            continue
except:
    print("Even number value is more than 20.")
    raise
finally:
    fact = 1
    for i in range(5, 0, -1):
        fact = fact*i

    print("Factorial of 5 :", fact)
    
"""
###### Provide different exception

try:
    num1 = 50
    num2 = 60
    print("division :", num1//2)
    assert num1 < num2
    print("addition:", num1 + "Hello")
except TypeError:
    print("Can not add int with string")
except AssertionError:
    print("both the numbers are not equal")
except WindowsError:
    pass
except ZeroDivisionError:
    print("Can not divide number by zero")