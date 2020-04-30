r = int(input("Input Revenue in RUB:"))
c = int(input("Input Costs in RUB:"))
e = int(input("Input number of Employees:"))
p = r - c
if r > c:
    print("You succeed")
    print("Your profit equals " + "{:2.2f}".format(p) + " RUB")
    print("Your return on revenue equals " + "{:.2f}".format((p / r) * 100) + " %")
    print("Your revenue per employee equals " + "{:.2f}".format(r / e) + " RUB")
else:
    print("You suffer losses!")
