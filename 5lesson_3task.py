tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', "Виталий", "Алексей", "Вован", "Костя"]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) > len(klasses):
    idx = len(tutors) - len(klasses)
    for _ in range(idx):
        klasses.append(None)

print(list(zip(tutors, klasses)))
