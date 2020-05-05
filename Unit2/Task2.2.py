change_list = input("Input a list, use ',' sign to separate units:")
change_list = change_list.split(",")
print(change_list)
i = 0
for i in range(0, len(change_list) - 1, 2):
    change_list[i], change_list[i + 1] = change_list[i + 1], change_list[i]
print(change_list)
