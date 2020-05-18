class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": float(salary), "bonus": float(bonus)}


class Position(Worker):

    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("salary") + self._income.get("bonus")


a = Position(input("Имя: "), input("Фамилия: "), input("Должность: "), input("Оклад: "), input("Бонус: "))
print(a.get_full_name())
print(a.position)
print(f"{a.get_total_income():.2f} рублей")
