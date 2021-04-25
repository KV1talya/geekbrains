class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_coat_square(self):
        return self.width / 6.5 + 0.5

    def get_jacket_square(self):
        return self.height * 2 + 0.3

    @property
    def get_full_square(self):
        square = self.get_coat_square() + self.get_jacket_square()
        return f"Общая площадь ткани {square}"


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.get_coat_square())

    def __str__(self):
        return f'Площадь, требуемая для пальто {self.square_c}'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.get_jacket_square())

    def __str__(self):
        return f'Площадь, требуемая на костюм {self.square_j}'


coat = Coat(5, 9)
jacket = Jacket(2, 3)
print(coat)
print(jacket)
print(coat.get_full_square)
print(jacket.get_full_square)
print(jacket.get_coat_square())
print(jacket.get_jacket_square())
