"""
class :  Class is nothing but a blueprint of any object is being created, and there we all
properties, attributes and functionality

object : object is the entity through we can access all the properties and attributes of any class.
method : The function we defined inside the is become method.
variable :
constructor :  Constructor initialize the memory of the object
             def __init___()
            -> default constructor
            -> Parametrize constructor

self : self is nothing but the object of the same class.

Inheritance
Polymorphism
Incapsulation
Abstraction
"""

class car:
    def __init__(self, car_name, car_price):
        # instance variable
        self.my_car_name = car_name
        self.car_price = car_price

    # object method/ instance method
    def print_car_name(self):
        print("My can name is AudiQ3")

    def show_car_name(self):
        print("New Car name ", self.my_car_name)

    def print_car_company(self, company):
        print(f"Car company name : {company}")

    def show_car_price(test):
        print("car price:", test.car_price)

    def show_All_details(self):
        self.show_car_name()
        self.show_car_price()



# obj = car()
# obj.print_car_name()
#
# print(obj.__module__)
# print(obj.__class__)
# print(__name__)
# print("_"*50)

if __name__ == '__main__':
    print("If condition executed")
    # obj = car()
    # obj.print_car_name()
    # print(obj.__module__)
    # print(obj.__class__)

    obj = car('BMW', '40Lac')
    #obj.print_car_name()
    #obj.show_car_name()
    #obj.show_car_price()
    #print("_"*50)
    #obj2 = car('Fortuner', '60Lac')
    #obj2.show_car_name()
    #obj2.print_car_company('Toyota')
    #obj2.show_car_price()
    #obj2.show_All_details()

    car.show_car_price(obj)





