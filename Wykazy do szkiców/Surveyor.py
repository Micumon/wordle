class Point:
    def __init__(self, number, x="0.0", y="0.0", h=None):
        self.number = number
        self.x = float(x)
        self.y = float(y)
        self.h = float(h) if h is not None else None

    def __str__(self):
        if self.h is not None:
            return f"{self.number} {self.x} {self.y} {self.h}"
        else:
            return f"{self.number} {self.x} {self.y}"


path_list = "Z:\\$$01_Winkalk\\@Winkalk 2023\\080_2023 Piłsudskiego 141\\szkic 1.txt"
path_coord = "Z:\\$$01_Winkalk\\@Winkalk 2023\\087_2023 Dostawcza 5\\Dostawcza 5.txt"
path_result = "Z:\\$$01_Winkalk\\@Winkalk 2023\\080_2023 Piłsudskiego 141\\wsad 1"


class PointsList:
    @staticmethod
    def __find_in_list(lista, item):
        for i in range(len(lista)):
            if lista[i] == item:
                return int(i)

    @staticmethod
    def __line_parser(text):
        text = text.strip().replace("\t", " ").replace(",", ".").replace("  ", " ").replace("  ", " ").replace("  ", " ")
        return text

    def __init__(self, path_coord, points=None):
        self.number = []
        self.X = []
        self.Y = []
        self.H = []
        self.i = 0
        if points is None:
            self.__builder_with_coords(path_coord)
        else:
            self.__builder_without_coords(path_coord, points)

    def __str__(self):
        print_str = ""
        if self.H is None:
            for i in range(len(self)):
                print_str += f"{self.number[i]} {self.X[i]} {self.Y[i]}\n"
        else:
            for i in range(len(self)):
                print_str += f"{self.number[i]} {self.X[i]} {self.Y[i]} {self.H[i]}\n"
        return print_str

    def __next__(self):
        if self.i <= len(self) - 1:
            next_str = f"{self.number[self.i]} {self.X[self.i]} {self.Y[self.i]}"
            self.i += 1
            return next_str
        else:
            self.i = 0
            raise StopIteration()

    def __iter__(self):
        return self

    def __contains__(self, item):
        if self[item] is not None:
            return True
        else:
            return False

    def __len__(self):
        return len(self.number)

    def __getitem__(self, item):
        try:
            i = PointsList.__find_in_list(self.number, str(item))
            if self.H:
                return self.X[i], self.Y[i], self.H[i]
            else:
                return self.X[i], self.Y[i]
        except TypeError:
            return None

    def __builder_with_coords(self, path_coord):
        with open(path_coord) as file:
            for line in file:
                if len(line) > 1:
                    list_line = self.__line_parser(line).split(" ")
                    self.number.append(list_line[0].rstrip())
                    self.X.append(list_line[1].rstrip())
                    self.Y.append(list_line[2].rstrip())
                    if len(list_line) == 4:
                        self.H.append(list_line[3].rstrip())
        if self.H:
            pass
        else:
            self.H = None

    def __builder_without_coords(self, path, points):
        with open(path, "r") as file:
            numbers = file.read().split(" ")
        for number in numbers:
            if len(number) > 0:
                self.number.append(number)
                self.X.append(points[number.strip()][0])
                self.Y.append(points[number.strip()][1])
                if points.H is not None:
                    self.H.append(points[number.strip()][2])
        if self.H:
            pass
        else:
            self.H = None


points = PointsList(path_coord)
