my_list = ["Hello!", 123, 123.1, ("one", "two", "three"), {"a", "b", "c"}, {"one": 1, "two": 2, "three": 3}, True]
i = 0
while i < len(my_list):
    print(f" {i+1} {my_list[i]} {str(type(my_list[i]))[8:-2:]}")
    i += 1
