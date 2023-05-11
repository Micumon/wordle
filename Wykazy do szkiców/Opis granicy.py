from Surveyor import *
import math


class TravelGen:
    def __init__(self):
        self.__counter = 0

    def __next__(self):
        if self.__counter == 0:
            self.__counter += 1
            return "biegnie"
        elif self.__counter == 1:
            self.__counter += 1
            return "zmierza"
        elif self.__counter == 2:
            self.__counter = 0
            return "podąża"


class NextPointGen:
    def __init__(self):
        self.__counter = 0
        self.__i = 0
        self.__points = None

    def next(self, i, points):
        self.__i = i
        self.__points = points
        if self.__counter == 0:
            self.__counter += 1
            return f". W punkcie {self.__points.number[self.__i]} granica"
        elif self.__counter == 1:
            self.__counter += 1
            return ", następnie"
        elif self.__counter == 2:
            self.__counter += 1
            return ". Dalej granica"
        elif self.__counter == 3:
            self.__counter = 0
            return ", w którym"


class ChangeDirGen:
    def __init__(self):
        self.__counter = 0

    def __next__(self):
        if self.__counter == 0:
            self.__counter += 1
            return "skręca"
        elif self.__counter == 1:
            self.__counter += 1
            return "odbija"
        elif self.__counter == 2:
            self.__counter = 0
            return "zmienia kierunek"


def desc_writer(points):
    direct = ""
    same_dir_times = 0
    result = ""
    for i in range(len(points)):
        if i == len(points) - 1:
            result += f" do punktu {points.number[i]}, od którego rozpoczęto opis."
            return result
        elif i == 0:
            direct = direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i + 1]),
                                            float(points.Y[i + 1])))
            result += f"{points.number[i]} na {direct}"
        elif direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i + 1]),
                                    float(points.Y[i + 1]))) == direct and same_dir_times == 0:
            same_dir_times += 1
            if direction(azimuth_calc(float(points.X[i + 1]), float(points.Y[i + 1]), float(points.X[i + 2]),
                                      float(points.Y[i + 2]))) == direct:
                result += f" przez punkty {points.number[i]}"
            else:
                result += f" przez punkt {points.number[i]}"
        elif direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i + 1]),
                                    float(points.Y[i + 1]))) == direct and same_dir_times > 0:
            result += f", {points.number[i]}"
        elif direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i + 1]),
                                    float(points.Y[i + 1]))) != direct:
            same_dir_times = 0
            direct = direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i + 1]),
                                            float(points.Y[i + 1])))
            result += f" do punktu {points.number[i]}{next_point.next(i, points)} {next(change_dir_gen)} " \
                      f"na {direct} i {next(travel_gen)}"


def direction(azimuth):
    if 375 <= azimuth <= 400 or 0 <= azimuth <= 25:
        return "północ"
    elif 25 < azimuth < 75:
        return "północny wschód"
    elif 75 <= azimuth <= 125:
        return "wschód"
    elif 125 < azimuth < 175:
        return "południowy wschód"
    elif 175 <= azimuth <= 225:
        return "południe"
    elif 225 < azimuth < 275:
        return "południowy zachód"
    elif 275 <= azimuth <= 325:
        return "zachód"
    elif 325 < azimuth < 375:
        return "północny zachód"


def azimuth_calc(Xp, Yp, Xk, Yk):
    dX = Xk - Xp
    if dX == 0:
        dX = 0.000001
    dY = Yk - Yp
    azimuth = math.atan(dY / dX) * 200 / math.pi
    if dX >= 0 and dY >= 0:
        return azimuth
    elif dX < 0 < dY:
        return 200 + azimuth
    elif dX < 0 and dY < 0:
        return 200 + azimuth
    elif dX > 0 > dY:
        return 400 + azimuth


change_dir_gen = ChangeDirGen()
travel_gen = TravelGen()
next_point = NextPointGen()
plot = "156/6"
description = f"""Granica działki {plot} {next(travel_gen)} od punktu {desc_writer(points)}"""

with open("C:\\Users\\admin\\Desktop\\proba\\opis.txt", "w") as file:
    file.write(description)
