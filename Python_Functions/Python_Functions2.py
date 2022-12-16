"""
Scope of the variable
Local Variable : Local variable limited to the function only
Global Variable :
    -> Global variable scope is available across the function in the module
    -> If we change value of global variable in the function, then we have to use
        global keyword
    -> if we define a local variable with same name as global then local value will get
        preference, which limited to that function only.

Non Local variable :
      ->  non local variable scope is limited to all inner function
      ->
"""



# global variable
varx = 100

def function1():
    print("We are in function1")
    #global varx
    #varx = 200
    vary = 60 # local variable
    print("varx:", varx)
    print("vary:", vary)

def function2():
    print("We are in function2")
    global varx
    varx = 300
    varz = 70 # local variable
    print("varx:", varx)
    print("vary:", varz)

"""
function1()
print("_"*40)
function2()
print("_"*40)
function1()
"""


# Non Local variable

# Global variable
varp = 500

def outer_function():
    # non local variable
    varq = 600

    def inner_fun1():
        print("we are in inner fun1")
        varu = 700
        print("varp global:", varp)
        print("varq non local:", varq)
        print("varu local:", varu)

    def inner_fun2():
        print("we are in inner fun2")
        nonlocal varq
        vart = 800
        varq = 900
        print("varp global:", varp)
        print("varq non local:", varq)
        print("vart local:", vart)

    inner_fun1()
    print("_"*50)
    inner_fun2()
    print("_" * 50)
    inner_fun1()

#def outer_function2():
    #print(var)
#outer_function()



#

var= "Hello"
var.upper()


def get_square_of_all(*args):
    """
    This function will provide you square of all the numbers that
    we are going to provide as list
    :param args:
    :return:
    """
    for val in args:
        print(val, ":", val**2)


#get_square_of_all(9, 6, 7, 3, 8, 2, 5)

#print(get_square_of_all.__doc__)


def addition(var1 : int, var2: int):
    return var1+ var2

print(addition('Hello', 'good'))

print(addition(70, 50))