def my_fun(name, second_name, birth, address, email, phone_number):
    print(name, second_name, birth, address, email, phone_number)


my_fun(name=input("Input your name: "), second_name=input("Input your second name: "),
       birth=input("Input your year of birth: "),
       address=input("Input your city of living: "), email=input("Input your E-mail: "),
       phone_number=input("Input your phone number: "))
