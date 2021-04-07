def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


print(type(nums_generator(15)))
for _ in nums_generator(15):
    print(_)


g = (x for x in range(1, 15 + 1, 2))
print(type(g))
for _ in g:
    print(_)
