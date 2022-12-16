"""
Method overriding : if parent class and child class have same method name, then child class method will
                    get preference
Method Overloading : python does support, of we have two method with same name in same class then latest
                    defined method will be considered.
"""


class A:
    def __init__(self, p, q, r):
        self._p = p
        self.__q = q
        self.r = r

    # Instance Method/Object Method
    def _addition(self):
        print("addition:", self._p + self.__q)

    def __multiplication(self):
        print(f"Multiplication of the values {self._p}, {self.__q}, {self.r} : {self._p*self.__q*self.r}")

    def subtraction(self):
        print("sutraction :", self._p - self.__q)

    # Class Method



if __name__ == '__main__':
    obj = A(30, 40, 50)
    obj._addition()
    print(obj._p)
    # Access variable/method with double underscore, _class__var/method
    print(obj._A__q)
    obj._A__multiplication()
