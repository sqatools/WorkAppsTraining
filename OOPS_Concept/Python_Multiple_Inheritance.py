

class A:
    def __init__(self, var1):
        self.var1 = var1

    def method_a(self):
        print("we are in class A")
        print("value of var1 : ", self.var1)


class B:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def method_b(self):
        print("we are in class B")
        print(f"value of p :{self.p} and q {self.q} : ")

# MRO : Method resolution Order
class C(A, B):
    def __init__(self, x, p, q, var1):
        #super(C, self).__init__(var1)
        self.x = x
        self.obja = A(var1)
        self.objb = B(p, q)

    def method_c(self):
        print("we are in class C")
        print(f"value of x : {self.x}")

if __name__ == '__main__':
    obj = C(50, 100, 200, 500)
    obj.objb.method_b()
    obj.obja.method_a()
    obj.method_c()
