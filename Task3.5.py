def my_fun():
    sum = 0
    contin = True
    while contin == True:
        n = input("Input a list of numbers, use space to separate. Q for quit: ").split()
        s = 0
        for el in range(len(n)):
            if ord(n[el]) == 81 or ord(n[el]) == 113:
                contin = False
                break
            else:
                s = s + int(n[el])
        sum = sum + s
        print(f"Subtotal sum equals {sum}")
    print(f"Total sum equals {sum}")


my_fun()
