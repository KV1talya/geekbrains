from requests import get, utils


def currency_rates(currency_code):
    current_rates_site = "http://www.cbr.ru/scripts/XML_daily.asp"
    current_rates = {}
    response = get(current_rates_site)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    word_list_tmp = ""
    for symbol in content:
        if symbol == "<":
            word_list_tmp += f"'{symbol}"
        elif symbol == ">":
            word_list_tmp += f"{symbol}'"
        else:
            word_list_tmp += symbol
    tmp_list = word_list_tmp.split("'")
    for n in range(len(tmp_list)):
        if tmp_list[n] == "<CharCode>":
            charcode = tmp_list[n + 1]
        elif tmp_list[n] == "<Value>":
            value = tmp_list[n + 1]
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
