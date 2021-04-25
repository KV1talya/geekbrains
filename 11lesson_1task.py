class Date:

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split("-"):
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2030 >= year >= 0:
                    return f'OK'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


print(Date.extract('25-04-2021'))
print(Date.valid(11, 11, 2022))
print(Date.valid(11, 13, 2011))

