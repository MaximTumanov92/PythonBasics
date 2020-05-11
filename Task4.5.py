from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)


def my_fun(el, el1):
    return el * el1


print(f"Произведенеи четных чисел от 100 до 1000 составляет: {reduce(my_fun, my_list)}")
