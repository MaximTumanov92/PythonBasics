from itertools import count, cycle

rpt = int(input("Times to repeat: "))
repeats = 0
my_list = [123, True, "Come on", [1, 2, 3]]
for el in cycle(my_list):
    if repeats > (rpt - 1):
        break
    print(my_list)
    repeats += 1
