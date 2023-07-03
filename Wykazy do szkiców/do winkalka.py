path = "C:\\Users\\admin\\Desktop\\Wykazy\\wykazy współrzędnych\\Szkic 1.txt"


def sorter(item):
    if item.isdigit():
        return int(item)
    else:
        number = ""
        for letter in item:
            if letter.isdigit():
                number += letter
            else:
                continue
        return 99999 + int(number)


with open(path, "r") as file:
    line = file.read()
line = line.strip().split(" ")
line.sort(key=sorter)

with open(path, "a") as file:
    file.write("\n")
    dash = 0
    for i in range(len(line)):
        if line[i].isdigit():
            if line[i + 1].isdigit() and int(line[i]) + 1 == int(line[i + 1]) and dash == 0:
                dash += 1
                file.write("," + line[i])
            elif line[i + 1].isdigit() and int(line[i]) + 1 == int(line[i + 1]) and dash > 0:
                dash += 1
            elif line[i + 1].isdigit() and int(line[i]) + 1 != int(line[i + 1]) and dash > 0:
                dash = 0
                file.write(" " + line[i])
            else:
                file.write("," + line[i])
        else:
            file.write("," + line[i])

