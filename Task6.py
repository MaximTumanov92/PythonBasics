a = float(input("Input Your first day distance:"))
b = float(input("Input Your goal:"))
day = 1
while b >= a:
    a = 1.1 * a
    day = day + 1
print("You`ll succeed on day " + str(day) + ".")
