list_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_data.insert(1, '"')
list_data.insert(3, '"')
list_data.insert(5, '"')
list_data.insert(7, '"')
list_data.insert(12, '"')
list_data.insert(14, '"')

list_data.remove("5")
list_data.insert(2, "05")

list_data.remove("+5")
list_data.insert(13, "+05")

print(list_data)
print(
    f"{list_data[0]} {list_data[1]}{list_data[2]}{list_data[3]} {list_data[4]} {list_data[5]}{list_data[6]}{list_data[7]} "
    f"{list_data[8]} {list_data[9]} {list_data[10]} {list_data[11]} {list_data[12]}{list_data[13]}{list_data[14]} {list_data[15]}")

print("\nПоиск чисел в списке:")
for number in list_data:
    if number.isdigit():
        print(f"Без знака: {number}")
    if number.startswith("+") or number.startswith("-"):
        print(f"Со знаком: {number}")
