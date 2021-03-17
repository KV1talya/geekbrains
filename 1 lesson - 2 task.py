list_number = []
summ = 0
summ_mod = 0


for number in range(1001):
    number = number**3
    if number % 2:
        list_number.append(number)

for idx in range(len(list_number)):
    len_number = len(str(list_number[idx]))
    number = list_number[idx]
    tmp_number = 0
    for i in str(number):
        tmp_number = tmp_number + int(i)
    if tmp_number%7 == 0:
        summ = summ + list_number[idx]

for idx_mod in range(len(list_number)):
    len_number_mod = len(str(list_number[idx_mod]+17))
    number_mod = list_number[idx_mod]+17
    tmp_number_mod = 0
    for i_mod in str(number_mod):
        tmp_number_mod = tmp_number_mod + int(i_mod)
    if tmp_number_mod%7 == 0:
        summ_mod = summ_mod + (list_number[idx_mod]+17)

print(summ)
print(summ_mod)