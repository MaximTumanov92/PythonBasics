from sys import argv

wages, hours, rate, bonus = argv
total_paid = int(hours) * int(rate) + int(bonus)
print(f"Будет выплачено {total_paid:.2f}")
