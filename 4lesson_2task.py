from requests import get, utils


def currency_rates(currency_code):
    current_rates_site = "http://www.cbr.ru/scripts/XML_daily.asp"
    current_rates = {}
    response = get(current_rates_site)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    word_list_tmp = content.replace("<", "'").replace(">", "'").split("'")
    n = 0
    for word in word_list_tmp:
        n += 1
        if word == "CharCode":
            charcode = (word_list_tmp[n])
        elif word == "Value":
            value = word_list_tmp[n]
            current_rates.update({charcode: value})
    currency_code = currency_code.upper()
    if current_rates.get(currency_code) == None:
        return ("None")
    else:
        current_rates_float = float(current_rates.get(currency_code).replace(",", "."))
        return (current_rates_float)


print(currency_rates("usd"))
print(type(currency_rates("USD")))

print(currency_rates("EUR"))
print(type(currency_rates("EUR")))

print(currency_rates("ave"))
