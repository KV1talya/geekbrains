def thesaurus(*arg):
    dict = {}
    for name in arg:
        if name[:1] in dict:
            dict[name[:1]].append(name)
        else:
            dict.update({name[:1]: [name]})
    print(dict)


thesaurus("Иван", "Мария", "Петр", "Илья", "Игорь", "Маша", "Паша", "Миша", "Михаил")
# thesaurus("Иван", "Мария", "Петр", "Илья")
