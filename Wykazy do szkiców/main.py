path_list = "Z:\\$$01_Winkalk\\@Winkalk 2023\\080_2023 Piłsudskiego 141\\szkic 1.txt"
path_coord = "Z:\\$$01_Winkalk\\@Winkalk 2023\\080_2023 Piłsudskiego 141\\punkty.txt"
path_result = "Z:\\$$01_Winkalk\\@Winkalk 2023\\080_2023 Piłsudskiego 141\\wsad 1"


def find_in_list(lista, obja):
    for i in range(len(lista)):
        if lista[i] == obja:
            return int(i)


class Points:
    def __init__(self, path_coord):
        self.number = []
        self.X = []
        self.Y = []
        self.H = []
        self.i = 0
        with open(path_coord) as file:
            for line in file:
                if len(line) > 1:
                    list_line = line.split(" ")
                    self.number.append(list_line[0].rstrip())
                    self.X.append(list_line[1].rstrip())
                    self.Y.append(list_line[2].rstrip())
                    if len(list_line) == 4:
                        self.H.append(list_line[3].rstrip())

    def __str__(self):
        print_str = ""
        if len(self.H) == 0:
            for i in range(len(self.number)):
                print_str += f"{self.number[i]} {self.X[i]} {self.Y[i]}\n"
        else:
            for i in range(len(self.number)):
                print_str += f"{self.number[i]} {self.X[i]} {self.Y[i]} {self.H[i]}\n"
        return print_str

    def __next__(self):
        if self.i <= len(self.number) - 1:
            next_str = f"{self.number[self.i]} {self.X[self.i]} {self.Y[self.i]}"
            self.i += 1
            return next_str
        else:
            self.i = 0
            raise StopIteration()

    def __iter__(self):
        return self

    def __contains__(self, item):
        return False


class ListPoints(Points):
    def __init__(self, path, points):
        self.number = []
        self.X = []
        self.Y = []
        self.H = []
        self.i = 0
        with open(path, "r") as file:
            numbers = file.read().split(" ")
        for number in numbers:
            if len(number) > 0:
                self.number.append(number.rstrip())
                i = find_in_list(points.number, number.rstrip())
                self.X.append(points.X[i])
                self.Y.append(points.Y[i])
                if len(points.H) >= 1:
                    self.H.append(points.H[i])


points = Points(path_coord)
list_points = ListPoints(path_list, points)
"""
with open(path_result, "w") as file:
    file.write(str(list_points))
   """
for i in points:
    print(i)

for i in points:
    print(i)
