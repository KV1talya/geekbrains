def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


print(type(nums_generator(15)))
for _ in nums_generator(15):
    print(_)


def nums_generator2(max_num):
    return (x for x in range(1, max_num + 1, 2))


print(type(nums_generator2(15)))
for _ in nums_generator2(15):
    print(_)
