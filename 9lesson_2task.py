class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def summ(self):
        self.calc_summ = self._length * self._width * self.weight * self.height // 1000
        print(self.calc_summ)


r = Road(20, 5000)
r.summ()
