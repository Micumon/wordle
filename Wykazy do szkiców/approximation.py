def approximation(length, h_max, h_min, h_looked):
    return (length*(h_looked-h_min))/(h_max-h_min)


end = False
searched_h = float(input("Podaj szukaną wysokość:  ").replace(",", "."))

while not end:
    h_minimum = float(input("Podaj minimalną wysokość:  ").replace(",", ".").strip())
    h_maximum = float(input("Podaj maksymalną wysokość:  ").replace(",", ".").strip())
    length_between = float(input("Podaj odległość:  ").replace(",", ".").strip())
    print(str(approximation(length_between, h_maximum, h_minimum, searched_h)))
    end = True if input("koniec?(T,N) ") == "T" else False

