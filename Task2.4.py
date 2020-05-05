my_string = input("Input a string, use space sign to separate words: ")
my_list = my_string.split(" ")
for ind, i in enumerate(my_list, 1):
    i = i[:10:]
    print(ind, i)
