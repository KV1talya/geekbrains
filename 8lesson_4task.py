def val_checker(func):
    def wrapper(x):
        if x > 0:
            print(func(x))
        elif x < 0:
            raise ValueError(x)

    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


calc_cube(5)
calc_cube(-5)
