def function1():
    print("Good Morning")

#function1()

def function2(msg):
    print(msg)


#function2('Hello How are you?')
#function2('Good afternoon everyone')

def addition(num1, num2):
    print("addition :", num1+num2)


# Pass by value
#addition(60, 50)

# Pass by reference
x = 500
y = 700
#addition(x, y)

# default value to param
def multiplication(num1, num2=60, num3=50):
    print("num3:", num3)
    print("num1:", num1)
    print("num2:", num2)
    print("Multiplication :", num1*num2)


#multiplication(5)
#multiplication(6, 80)
num2 = 40
num3 = 60
#multiplication(num3=90, num2=30, num1=num2+num3)

# *args : provide list of value in the function

def get_multiple_value(num1, *args):
    print("Num1 :", num1)
    print(args)
    for val in args:
        print(val)

#get_multiple_value(5, 6, 3, 8, 12, 'Python', (4, 6, 23))

# **kwargs : we can provide parameter values in the form on key value pair

def user_info(**kwargs):
    print(kwargs, type(kwargs))

    for key, value in kwargs.items():
        print(key ,":", value )


#user_info(name='rahul', email='rahul@gmail.com', mobile=655654654, city='Pune')

def login(**kwargs):
    db_username = 'adminuser'
    db_password = 'P@ssw0rd'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Access Denied, Wrong username password")

#login(username='adminuser', password='P@ssw0rd')
#output = login(username='admin', password='P@ssw0rd1')
#print(output)


def login_return(**kwargs):
    db_username = 'adminuser'
    db_password = 'P@ssw0rd'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        return "Login Successful"
    else:
        return "Access Denied, Wrong username password"

#output = login_return(username='admin', password='P@ssw0rd1')
#print(output)

def print_value(n):
    for i in range(n):
        if i == 5:
            return "completed"
        print(i)
#output = print_value(10)
#print("output :", output)
def addition(num1, num2=60):
    return num1+num2

def print_value2(n):
    for i in range(n):
        if i == 6:
            return True if i%2 == 0 else False
        print(i)
#var1 = print_value2(10)
#print("output :", var1)

def print_value3(n):
    for i in range(n):
        if i == 6:
            return addition(i)
        print(i)
var1 = print_value3(10)
print("output :", var1)

