seasons = {(12, 1, 2): "Winter", (3, 4, 5): "Spring", (6, 7, 8): "Summer", (9, 10, 11): "Autumn"}
month = input("Input number of the month: ")
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November",
               "December"]
while not month.isdigit():
    print("You are to input a number!")
    month = input("Try again.")
while not 1 <= int(month) <= 12:
    print("You are to input a number between 1 and 12!")
    month = input("Try again.")
month = int(month)
for i in seasons:
    for j in i:
        if j == month:
            answer = seasons.get(i)
print(f"Month # {month} is called {month_names[month - 1]} and comes in {answer}")
