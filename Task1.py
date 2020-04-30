name = "Name"
age = 0
weight = 1.5
story = 0

print("At his birth a person has no " + name + " and he`s age is just over " + str(
    age) + " years. He`s really small and weights a bit more than "
      + str(weight))
story = input("Want the same story about You? (Yes/No)")
while story != "Yes" and story != "No":
    print("You are to choose between Yes and No")
    story = input("Try again.")
if story == "No":
    print("Whatever")
else:
    name = input("Your Name?")
    age = int(input("Your age?"))
    weight = int(input("Your weight?"))
    print("You`re lucky " + name + ". No idea of your your weight at birth, but in your " + str(
        age) + " years your weight is " + str(weight) + " kgs. And it`s great!")
