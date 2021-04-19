class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

s = Stationery()
p = Pen()
pe = Pencil()
h = Handle()
s.draw()
p.draw()
pe.draw()
h.draw()