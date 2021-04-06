src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 11, 12, 55, 54]
result = []

number_tmp = src[0]
for number in src:
    if number > number_tmp:
        result.append(number)
    number_tmp = number

print(result)


