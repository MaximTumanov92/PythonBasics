from math import factorial

a = int(input("Input final number: "))


def generator():
    for i in range(1, a):
        yield i


g = generator()
print(g)

for el in g:
    print(factorial(el))
