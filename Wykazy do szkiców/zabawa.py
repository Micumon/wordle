from math import *


def n_element_list(n):
    element = int()
    result = []
    for el in range(n):
        result.append(element)
    return result


def sum_checker(com, search):
    res = list()
    for c in com:
        if sum(c) == search:
            res.append(c)
    return res


def nicer_combinations_generator(set_n, squares, combinations=None, counter=0, tup_res=()):
    if combinations is None:
        combinations = []
    for a in set_n:
        counter += 1
        tup_res += (a,)
        if counter <= squares:
            nicer_combinations_generator(set_n, squares, combinations, counter, tup_res)
        if len(set(tup_res)) == squares and set(tup_res) not in combinations:
            combinations.append(set(tup_res))
        tup_res = list(tup_res)
        tup_res.pop()
        tup_res = tuple(tup_res)
        counter -= 1


def combinations_generator(set_n, squares):
    combinations = []
    for a in set_n:
        if squares >= 2:
            for b in set_n:
                if squares >= 3:
                    for c in set_n:
                        if squares >= 4:
                            for d in set_n:
                                if squares >= 5:
                                    for e in set_n:
                                        if squares >= 6:
                                            for f in set_n:
                                                if squares >= 7:
                                                    for g in set_n:
                                                        if squares >= 8:
                                                            for h in set_n:
                                                                if len({a, b, c, d, e, f, g, h}) == 8 and \
                                                                        {a, b, c, d, e, f, g, h} not in combinations:
                                                                    combinations.append({a, b, c, d, e, f, g, h})
                                                        elif len({a, b, c, d, e, f, g}) == 7 and \
                                                                {a, b, c, d, e, f, g} not in combinations:
                                                            combinations.append({a, b, c, d, e, f, g})
                                                elif len({a, b, c, d, e, f}) == 6 and \
                                                        {a, b, c, d, e, f} not in combinations:
                                                    combinations.append({a, b, c, d, e, f})
                                        elif len({a, b, c, d, e}) == 5 and {a, b, c, d, e} not in combinations:
                                            combinations.append({a, b, c, d, e})
                                elif len({a, b, c, d}) == 4 and {a, b, c, d} not in combinations:
                                    combinations.append({a, b, c, d})
                        elif len({a, b, c}) == 3 and {a, b, c} not in combinations:
                            combinations.append({a, b, c})
                elif len({a, b}) == 2 and {a, b} not in combinations:
                    combinations.append({a, b})
        elif a and {a} not in combinations:
            combinations.append({a})
    return combinations


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
searched_sum = 6
squares_num = 5
#must_contain = 4
combinations_number = int(factorial(len(numbers)) / (factorial(squares_num) * factorial(len(numbers) - squares_num)))
combinations = []
nicer_combinations_generator(numbers, squares_num, combinations)
#result = sum_checker(combinations, searched_sum)

print(combinations)
print("Powinno być: " + str(combinations_number))
print("Jest: " + str(len(combinations)))

