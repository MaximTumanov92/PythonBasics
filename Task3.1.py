def my_fun(n_1, n_2):
    try:
        n_3 = n_1 / n_2
        return n_3
    except ZeroDivisionError:
        print("Digit must differ from Zero")


print(f"Result is {my_fun(int(input('Enter a digit: ')), int(input('Enter a digit: ')))}")
