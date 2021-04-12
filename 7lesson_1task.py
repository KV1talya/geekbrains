import os

current_dir = os.path.abspath(os.getcwd())


def create_dir(path):
    full_path = os.path.join(current_dir, path)
    if os.path.exists(full_path):
        pass
    else:
        os.makedirs(full_path)


def create_file(path):
    full_path = os.path.join(current_dir, path)
    if os.path.exists(full_path):
        pass
    else:
        with open(full_path, mode='a'):
            pass


with open("config.yaml", 'r', encoding='utf-8') as f:
    for data in f:
        if data[0:2] == "->":
            folder = data.split(" ")[1].replace(":", "")
            parent_folder = folder.replace("\n", "")
            create_dir(parent_folder)
        elif data[0:3] == "-->":
            folder = data.split(" ")[1].replace(":", "").replace("\n", "")
            files = data.split(":")[1].replace("\n", "")
            parent_folder_two = f"{parent_folder}/{folder}"
            create_dir(f"{parent_folder}/{folder}")
            for file in files.split(","):
                create_file(f"{parent_folder}/{folder}/{file.replace(' ', '')}")
        elif data[0:4] == "--->":
            folder = data.split(" ")[1].replace(":", "").replace("\n", "")
            files = data.split(":")[1].replace("\n", "")
            parent_folder_three = f"{parent_folder_two}/{folder}"
            create_dir(f"{parent_folder_two}/{folder}")
            for file in files.split(","):
                create_file(f"{parent_folder_two}/{folder}/{file.replace(' ', '')}")
        elif data[0:5] == "---->":
            folder = data.split(" ")[1].replace(":", "").replace("\n", "")
            files = data.split(":")[1].replace("\n", "")
            create_dir(f"{parent_folder_three}/{folder}")
            for file in files.split(","):
                create_file(f"{parent_folder_three}/{folder}/{file.replace(' ', '')}")
