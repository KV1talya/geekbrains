class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return self.quantity - other.quantity
        else:
            return 'Результат отрицательный'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, cells_in_row):
        row = ''
        cels = self.quantity // cells_in_row
        for i in range(cels):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        if row.endswith("\\n"):
            return row[:-2]
        else:
            return row


cells1 = Cell(12)
cells2 = Cell(15)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2 - cells1)
print(cells2 * cells1)
print(cells2 / cells1)
print(cells1.make_order(5))
print(cells2.make_order(5))

