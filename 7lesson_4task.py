import os

FIND_FOLDER = "some_data"
current_dir = os.path.abspath(os.getcwd())
full_path_find = os.path.join(current_dir, FIND_FOLDER)

size = {}

for root, dirs, files in os.walk(full_path_find):
    n100 = 0
    n1000 = 0
    n10000 = 0
    n100000 = 0
    for file in files:
        file_size = os.lstat(f"{full_path_find}/{file}")[6]
        if file_size <= 100:
            n100 += 1
            size.update({1000: n100})
        elif file_size <= 1000:
            n1000 += 1
            size.update({1000: n1000})
        elif file_size <= 10000:
            n10000 += 1
            size.update({10000: n10000})
        elif file_size <= 100000:
            n100000 += 1
            size.update({100000: n100000})
print(size)
