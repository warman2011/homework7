class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            return f'Количество клеток не может быть отрицательным...'
        pass
    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return round(self.cell / other.cell)

    # def __repr__(self):
    #     return "Cell()"

    # def __str__(self):
    #     return f'lkbkmcblc{Cell(self)}'
    def make_order(self, order):
        self.order = order
        if self.cell % self.order != 0:
            return (f"{'*' * self.order}"+"\\n") * (self.cell//self.order) + (f"{'*'* (self.cell % self.order)}")
        else:
            return ((f"{'*' * self.order}" + "\\n") * (self.cell // self.order))[:-2]

cells1 = Cell(10)
cells2 = Cell(3)

print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 / cells2)
print(cells1 * cells2)
print(cells1.make_order(6))

