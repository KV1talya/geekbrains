import re


def email_parse(email: str) -> dict:
    email_return = {}
    if re.match(r'^[0-9A-Za-z]+@[0-9A-Za-z]+\.[A-Za-z]\D+', email):
        username, domain = email.split("@")
        email_return.update({"username": username, "domain": domain})
        return email_return
    else:
        raise ValueError(email)


if __name__ == '__main__':
    print(email_parse("someone@geekbrains.ru"))
    print(email_parse("someone@geekbrainsru"))
    # print(email_parse("someone%geekbrains.ru"))
