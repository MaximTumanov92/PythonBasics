class Road:
    def __init__(self, _length, _width, _cm, _depth):
        self._length = _length
        self._width = _width
        self._cm = _cm
        self._depth = _depth

    def weight(self):
        return self._length * self._width * self._cm * self._depth


class MassCount(Road):
    def __init__(self, _length, _width, _cm, _depth):
        super().__init__(_length, _width, _cm, _depth)


result = MassCount(int(input("Введите длину дороги: ")), int(input("Введите ширину дороги: ")),
              int(input("Введите вес 1 см покрытия  1 м*2 дороги: ")), int(input("Введите толщину покрытия дороги: ")))
print(result.weight())
