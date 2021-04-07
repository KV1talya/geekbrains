tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', "Виталий", "Алексей", "Вован", "Костя"]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) > len(klasses):
    idx = len(tutors) - len(klasses)
    for _ in range(idx):
        klasses.append(None)

print("Не генератор")
print(list(zip(tutors, klasses)))


tutors2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', "Виталий", "Алексей", "Вован", "Костя"]
klasses2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def nums_generator2(tutors,klasses):
    if len(tutors) > len(klasses):
        idx = len(tutors) - len(klasses)
        for _ in range(idx):
            klasses.append(None)
    yield list(zip(tutors, klasses))

print("Генератор")
print(type(nums_generator2(tutors2, klasses2)))
for x in nums_generator2(tutors2,klasses2):
    print(x)