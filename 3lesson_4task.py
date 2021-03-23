def thesaurus_adv(*arg):
    dict = {}
    dict_sort = {}
    for full_name in arg:
        key_last_name = full_name.split(" ")[1][:1]
        key_first_name = full_name.split(" ")[0][:1]
        if key_last_name in dict:
            if key_first_name not in dict[key_last_name]:
                dict[key_last_name].update({key_first_name: [full_name]})
            else:
                dict[key_last_name][key_first_name].append(full_name)
        else:
            dict.update({key_last_name: {key_first_name: [full_name]}})
    print(dict)
    for sort in sorted(dict.keys()):
        dict_sort.update({sort: dict.get(sort)})
    print(dict_sort)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Андрей Сабирович",
              "Иван Иванович", "Анна Иванова")
