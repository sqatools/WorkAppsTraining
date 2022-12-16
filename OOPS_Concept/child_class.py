from OOPS_Concept.parent_class import father
from OOPS_Concept.constant_data import *
from OOPS_Concept.mother_class import mother
from OOPS_Concept.constant_base_class import ConstantBase

class son(father, mother):
    def __init__(self, sname,
                 fname=ConstantBase.fname,
                 fhouse=father_house,
                 fcar=father_car,
                 fbusiness=father_business,
                 gname=ConstantBase._gname,
                 gland=ConstantBase._ConstantBase__gproperty):
        super().__init__(fname,
                 fhouse,
                 fcar,
                 fbusiness,
                 gname, gland)
        self.sname = sname
        self.mobj = mother(mother_name, mother_Car)
        self.show_all_details_of_father()

    def show_son_name(self):
        print("Son name :", self.sname)

    def show_all_details_of_father(self):
        self.show_father_name()
        self.show_father_car()
        self.show_father_house_details()
        self.show_father_business()
        name = self.show_grand_parent_name()
        property = self.show_gparent_property()
        print(name, property)

if __name__ == '__main__':
    obj = son('Aditya')
    obj.show_all_details_of_father()
    # obj.mobj.show_mother_details()
    # obj.show_grand_parent_name()