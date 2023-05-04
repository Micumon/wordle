import main
import math


def opis_writer(points):
    direct = ""
    same_dir_times = 0
    resault = ""
    for i in range(len(points)):
        if i == len(points) - 1:
            resault += f"do punktu {points.number[i]}, od którego rozpoczęto opis."
            return resault
        elif i == 0:
            direct = direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i+1]), float(points.Y[i+1])))
            resault += f"{points.number[i]} biegnie na {direct}"
        elif direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i+1]), float(points.Y[i+1]))) == direct \
                and same_dir_times == 0:
            same_dir_times += 1
            resault += f" przez punkt {points.number[i]}"
        elif direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i+1]), float(points.Y[i+1]))) == direct \
                and same_dir_times > 0:
            resault += f", {points.number[i]}"
        elif direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i+1]), float(points.Y[i+1]))) != direct:
            same_dir_times = 0
            direct = direction(azimuth_calc(float(points.X[i]), float(points.Y[i]), float(points.X[i+1]), float(points.Y[i+1])))
            resault += f" do punktu {points.number[i]}. W punkcie {points.number[i]} skręca na {direct} i biegnie"


def direction(azymut):
    if 375 <= azymut <= 400 or 0 <= azymut <= 25:
        return "północ"
    elif 25 < azymut < 75:
        return "północny wschód"
    elif 75 <= azymut <= 125:
        return "wschód"
    elif 125 < azymut < 175:
        return "południowy wschód"
    elif 175 <= azymut <= 225:
        return "południe"
    elif 225 < azymut < 275:
        return "południowy zachód"
    elif 275 <= azymut <= 325:
        return "zachód"
    elif 325 < azymut < 375:
        return "północny zachód"


def azimuth_calc(Xp, Yp, Xk, Yk):
    dX = Xk - Xp
    if dX == 0:
        dX = 0.000001
    dY = Yk - Yp
    azimuth = math.atan(dY/dX)*200/math.pi
    if dX >= 0 and dY >= 0:
        return azimuth
    elif dX > 0 and dY < 0:
        return 200 + azimuth
    elif dX < 0 and dY < 0:
        return 200 + azimuth
    elif dX < 0 and dY > 0:
        return 400 + azimuth

azimuth_calc(100, 100, 101, 210)
dzialka = "156/6"
opis_body = opis_writer(main.points)
opis = f"""Granica działki {dzialka} od punktu {opis_body}"""

with open("C:\\Users\\admin\\Desktop\\proba\\opis.txt", "w") as file:
    file.write(opis)

