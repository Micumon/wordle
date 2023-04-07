class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    def __init__(self, cake_name, cake_kind, cake_taste, cake_additives, cake_filling):
        self.name = cake_name
        if cake_kind in Cake.known_types:
            self.kind = cake_kind
        else:
            self.kind = "other"
        self.taste = cake_taste
        self.additives = list(cake_additives).copy()
        self.filling = cake_filling
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(self.name.upper())
        print(f"Taste: {self.taste}")
        if self.additives:
            print("Additives: " + ", ".join(self.additives))
        if self.filling != "":
            print(f"Filling: {self.filling}")
        print("***************************")

    def set_filling(self, new_filling):
        self.filling = new_filling

    def add_additives(self, new_additives):
        for add in new_additives:
            self.additives.append(add)


vanila_cake = Cake("Vanila Cake","cake","vanilla", ["chocolade","nuts"], "cream")
chocolade_muffin = Cake("Chocolade Muffin", "muffin","chocolade", "", "")
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')



#vanila_cake.show_info()
#chocolade_muffin.show_info()
#chocolade_muffin.show_info()
#print(cake04.kind)


for position in Cake.bakery_offer:
    position.show_info()

print(isinstance(cake04,Cake))
print(type(cake04))
print(vars(cake04))
print(vars(Cake))
print(dir(Cake))
print(dir(cake04))
