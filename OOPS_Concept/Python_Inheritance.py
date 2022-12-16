"""
Inheritance : when one class aquire the property of another
class is knows as inheritance

1. Single Inheritance : Class A -> Class B  (father ->son)
2. Multi Level Inheritance : Class A -> Class B -> Class C
   (grand father -> father -> son)
3. Multiple Inheritance : Class A -> Class B, Class C -> Class B
   (father -> son, mother -> son)
"""
# Single Inheritance
class father:
    def __init__(self, fname, fhouse, fcar, fbusiness):
        self.fname = fname
        self.fhouse = fhouse
        self.fcar = fcar
        self.fbusiness = fbusiness

    def show_father_name(self):
        print("My father name is :", self.fname)

    def show_father_house_details(self):
        print("My fahter own luxury:", self.fhouse)

    def show_father_car(self):
        print("Father car name:", self.fcar)

    def show_father_business(self):
        print("Father has good business :", self.fbusiness)


class son(father):
    def __init__(self, sname, fname, fhouse, fcar, fbusiness):
        super().__init__(fname, fhouse, fcar, fbusiness)
        self.sname = sname

    def show_son_name(self):
        print("Son name :", self.sname)

    def show_all_details_of_father(self):
        self.show_father_name()
        self.show_father_car()
        self.show_father_house_details()
        self.show_father_business()


# if __name__ == '__main__':
#     print("We are in if condition")
#     obj = son('Aditya', 'SharmaJi', 'Bangalow', 'BMW', 'Construction')
#
#     obj.show_son_name()
#     obj.show_all_details_of_father()
#     print(obj.__module__)
#
print("We are in if condition")
obj = son('Aditya', 'SharmaJi', 'Bangalow', 'BMW', 'Construction')

obj.show_son_name()
obj.show_all_details_of_father()
print(obj.__module__)