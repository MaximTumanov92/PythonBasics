def my_fun(n_1, n_2, n_3):
    try:
        result = max(int(n_1) + int(n_2), int(n_2) + int(n_3), int(n_1) + int(n_3))
        print(result)
    except ValueError:
        print("Enter digits only")


my_fun(input("Enter first digit :"), input("Enter second digit :"), input("Enter third digit :"))
