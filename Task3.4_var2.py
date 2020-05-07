def my_fun(n_1, n_2):
    """Возведение в степень.
    Функция усложнена, относительно задания и возводит любое число в любую степень, используя цикл.
    n_1 - число
    т_2 - степень
    """
    initial_number = n_1
    if n_2 < 0:
        while abs(n_2) != 1:
            n_1 = n_1 * initial_number
            n_2 += 1
            result = 1 / n_1
    elif n_2 > 0:
        while abs(n_2) != 1:
            n_1 = n_1 * initial_number
            n_2 -= 1
            result = n_1
    else:
        result = 1

    return result


print(my_fun(int(input("Input a number: ")), int(input("Input a number: "))))
