number = int(input("Введите число от 1 до 20 или любое другое для вывода полного списка: "))


def percent(numbers):
   if numbers == 1:
      print(f"{numbers} процент")
   elif 1 < numbers <= 4:
      print(f"{numbers} процента")
   elif 5 <= numbers <= 20:
      print(f"{numbers} процентов")


if 0 < number <= 20:
   percent(number)
else:
   for percents in range(1, 21):
      percent(percents)
