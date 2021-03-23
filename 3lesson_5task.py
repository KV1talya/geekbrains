from random import randrange


def get_jokes(n: int):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_print = []
    for joke in range(n):
        joke_tmp = f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} {adjectives[randrange(len(adjectives))]}"
        joke_print.append(joke_tmp)
    print(joke_print)


get_jokes(6)
