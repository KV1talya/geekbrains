def type_logger(func):
    def wrapper(*args, **kwargs):
        for x in args:
            name_func = str(func).split(" ")[1]
            print(f'{name_func}({x}: {func(x)})', end=",")
        for x in kwargs:
            value = kwargs.get(x)
            name_func = str(func).split(" ")[1]
            print(f'{name_func}({x}={value}: {func(x)})', end=",")

    return wrapper


@type_logger
def calc_cube(x):
    return type(x)


def print_text():
    return ("test")


# calc_cube(2, "dddd", 4, "12312", print_text)
calc_cube(a=2, b="xxxx", c=4, d=12312, e=print_text)
