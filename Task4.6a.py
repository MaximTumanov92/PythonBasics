from itertools import count, cycle

a = int(input("Enter start number: "))
b = int(input("Input final number: "))
for el in count(a):
    if el > b:
        break
    else:
        print(el)