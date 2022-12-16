

class A:
    x = 60 # class variable
    y = 80 # class variable

    def __init__(self, p, q, r):
        self.p = p # instance variable
        self.q = q
        self.r = r

    def subtraction(self):
        print("subtraction :", self.p - self.q)

    # Class Method
    @classmethod
    def show_x_value(name):
        print("value of x:", name.x)
        #print(self.p)
        print("value of y:", A.y)

    def show_p_value(self):
        print("value of p :", self.p)

    @staticmethod
    def factorial_num(n):
        fact = 1
        for i in range(n, 0, -1):
            fact = fact *i

        print("factorial:", fact)




if __name__ == '__main__':
    #obj = A(30, 40, 50)
    # obj.show_x_value()
    # obj.show_p_value()
    # obj.x = 100
    # obj.p = 500
    # print(obj.x)
    # obj.show_x_value()
    # obj.show_p_value()

    #obj.factorial_num(5)
    A.factorial_num(6)  # calling static method with class name