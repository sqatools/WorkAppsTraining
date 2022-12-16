"""
Method overriding : if parent class and child class have same method name, then child class method will
                    get prefrence
Method Overloading : python does support, of we have two method with same name in same class then latest
                    defined method will be considered.
"""


class A:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    def addition(self):
        print("addition:", self.p + self.q)

    def multiplication(self):
        print(f"Multiplication of the values {self.p}, {self.q}, {self.r} : {self.p*self.q*self.r}")

class B(A):
    def __init__(self, p, q, x, y, z):
        super(B, self).__init__(x, y, z)
        self.p1 = p
        self.q1 = q

    def subtraction(self):
        print("subtraction:", self.p1 - self.q1)

    def multiplication(self):
        print(f"Multiplication of the values {self.p1}, {self.q1} : {self.p1*self.q1}")

    def print_msgs(self, msg1,  msg2):
        print("msg1", msg1)
        print("msg2", msg2)

    def print_msgs(self, msg1,  msg2, msg3):
        print("msg1", msg1)
        print("msg2", msg2)
        print("msg2", msg3)


if __name__ == '__main__':
    obj = B(10, 20, 30, 40, 50)
    # obj.subtraction()
    # obj.addition()
    # obj.__setattr__('p1', 60)
    # print(obj.p1)
    #
    # obj.subtraction()
    # print(obj.__getattribute__('q1'))

    #obj.multiplication()
    #obj.print_msgs('Hello', 'Good Morning', 'Good day')

num1 = 60
num2 = 70
print(num1 + num2)

print(num1.__add__(num2))

str1 = 'Python'
str2 = 'Programming'
print(str1 + str2)
print(str1.__add__(str2))

