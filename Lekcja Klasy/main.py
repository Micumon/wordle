import pickle
import glob

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, cake_name, cake_kind, cake_taste, cake_additives, cake_filling, gluten, text):
        self.name = cake_name
        if cake_kind in Cake.known_types:
            self.kind = cake_kind
        else:
            self.kind = "other"
        self.taste = cake_taste
        self.additives = list(cake_additives).copy()
        self.filling = cake_filling
        self.__gluten_free = gluten
        if cake_kind == "cake":
            self.__text = text
        else:
            self.__text = ""
        Cake.bakery_offer.append(self)

    @property
    def Text(self):
        return self.__text

    @Text.setter
    def Text(self, new_text):
        if self.kind == "cake":
            self.__text = new_text
        else:
            print(f"{self.name} is not cake!")

    def show_info(self):
        print(self.name.upper())
        print(f"Type: {self.kind}")
        print(f"Taste: {self.taste}")
        if self.additives:
            print("Additives: " + ", ".join(self.additives))
        if self.filling != "":
            print(f"Filling: {self.filling}")
        print(f"Gluten free: {self.__gluten_free}")
        if self.kind == "cake":
            print(f"Text on cake: \"{self.Text}\"")
        print("***************************")

    def set_filling(self, new_filling):
        self.filling = new_filling

    def add_additives(self, new_additives):
        for add in new_additives:
            self.additives.append(add)

    def save_to_file(self, path):
        with open(path,"wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as file:
            new_cake = pickle.load(file)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path)


vanila_cake = Cake("Vanila Cake","cake","vanilla", ["chocolade","nuts"], "cream", False, "Micu")
chocolade_muffin = Cake("Chocolade Muffin", "muffin","chocolade", "", "", True, "Micu")
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, "Micu")
vanila_cake.Text = "100 lat! Micu"
vanila_cake.save_to_file(r'C:\Users\admin\PycharmProjects\Lekcja Klasy\Save\vanila_cake.bakery')
cake04.save_to_file(r'C:\Users\admin\PycharmProjects\Lekcja Klasy\Save\cake04.bakery')
vanila_cake.Text = ""
cake05 = Cake.read_from_file(r'C:\Users\admin\PycharmProjects\Lekcja Klasy\Save\vanila_cake.bakery')

cake_list = Cake.get_bakery_files(r'C:\Users\admin\PycharmProjects\Lekcja Klasy\Save\*.bakery')

#vanila_cake.show_info()
#chocolade_muffin.show_info()
#chocolade_muffin.show_info()
#print(cake04.kind)


for position in Cake.bakery_offer:
    position.show_info()
print(cake_list)

