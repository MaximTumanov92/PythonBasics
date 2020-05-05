my_list = [7, 5, 3, 3, 2]
initial_len = len(my_list)
n = int(input("Input a number: "))
for i in range(len(my_list)):
    if n >= my_list[i] and initial_len == len(my_list):
        q = my_list.count(n)
        my_list.insert(i + q, n)
    elif n < my_list[len(my_list) - 1]:
        my_list.append(n)
print(my_list)
