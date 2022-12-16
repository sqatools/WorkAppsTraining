from OOPS_Concept.grand_parent_class import grandparent

class father(grandparent):
    def __init__(self, fname,
                 fhouse,
                 fcar,
                 fbusiness,
                 gname, gland):
        super(father, self).__init__(gname, gland)
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

    def show_his_father_name(self):
        return f"His father name is : {self.gname}"
