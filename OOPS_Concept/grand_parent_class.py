
class grandparent:
    def __init__(self, gname , land):
        self.land = land
        self.gname = gname

    def show_grand_parent_name(self):
        return f"Grand parent name: {self.gname}"

    def show_gparent_property(self):
        return f"Grand parent owns : {self.land}"
