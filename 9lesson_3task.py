class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": 'wage', "bonus": 'bonus'}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position(name="Petr", surname="Petrovich", wage=100, bonus=16)

print(position.get_full_name())
print(position.get_total_income())
