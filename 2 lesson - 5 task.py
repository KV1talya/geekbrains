price = [57.8, 46.51, 97, 33, 1, 18.8, 99.9, 199.9, 88, 77, 88.8, 33.9, 55.7, 0.99]
price_down = []
text_out = ""
text_out_down = ""

for number in price:
    if type(number) == int:
        text_out += f"{number} руб 00 коп, "
    elif type(number) == float:
        rub = str(number).split(".")[0]
        kop = str(number).split(".")[1]
        if len(kop) == 1:
            kop = f"0{kop}"
        text_out += f"{rub} руб {kop} коп, "

print(text_out)

price.sort()
print(price)

for price_d in price:
    price_down.append(price_d)

price_down.sort(reverse=True)
print(price_down)

n = 0
for five in price:
    text_out_down += f"{five} "
    n += 1
    if n == 5:
        break
print(text_out_down)
