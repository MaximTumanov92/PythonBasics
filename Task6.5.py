class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
            return f"Запуск отрисовки {self.title}"


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы используете {self.title[:-1]}у. {Stationary.draw(self)[:-1]}ой"


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы используете {self.title}. {Stationary.draw(self)}ом"


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы используете {self.title}. {Stationary.draw(self)}ом"


pen = Pen('Ручка')

pencil = Pencil('Карандаш')

handle = Handle('Маркер')

print(pen.draw())

print(pencil.draw())

print(handle.draw())
