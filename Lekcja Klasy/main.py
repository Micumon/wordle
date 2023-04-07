class Cake:
    def __init__(self, cake_name, cake_kind, cake_taste, cake_additives, cake_filling):
        self.name = cake_name
        self.kind = cake_kind
        self.taste = cake_taste
        self.additives = cake_additives
        self.filling = cake_filling

    def show_info(self):
        print(self.name)

vanila_cake = Cake("Vanila Cake","cake","vanilla", ["chocolade","nuts"], "cream")
chocolade_muffin = Cake("Chocolade Muffin", "muffin","chocolade","", "")


menu = [vanila_cake,chocolade_muffin]

for position in menu:
    print(f"{position.name} - ({position.kind}) main taste: {position.taste} with additives of {position.additives}"
          f", filled with {position.filling}")