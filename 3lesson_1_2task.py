def num_translate_adv(word: str):
    word_list = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                 "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if word == word.title():
        print(f"{str(word_list.get(word.lower())).title()}")
    else:
        print(f"{str(word_list.get(word))}")


num_translate_adv("one")
num_translate_adv("One")

num_translate_adv("three")
num_translate_adv("Three")

num_translate_adv("Ten")
num_translate_adv("ten")

num_translate_adv("eleven111")
num_translate_adv("Eleven")
