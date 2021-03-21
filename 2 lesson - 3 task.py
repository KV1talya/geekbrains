list_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

for name in list_name:
    name_title = name.split(" ")[-1]
    print(f"Привет, {name_title.title()}!")
