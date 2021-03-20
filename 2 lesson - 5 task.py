price = [57.8, 46.51, 97, 33, 1, 18.8, 99.9, 199.9, 88, 77, 88.8, 33.9, 55.7, 0.99]
text_out = ""

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
