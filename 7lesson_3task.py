import os

PROJECT_NAME = "my_project"
TEMPLATE_FOLDER = "templates"
FORMAT_FILE = "html"

current_dir = os.path.abspath(os.getcwd())
full_path_project = os.path.join(current_dir, PROJECT_NAME)


def create_dir(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)


def create_file(path):
    if os.path.exists(path):
        pass
    else:
        with open(path, mode='a'):
            pass


for root, dirs, files in os.walk(full_path_project):
    for file in files:
        if file.split(".")[1] == FORMAT_FILE:
            folder = root.split("/")[-1:][0]
            new_file = os.path.join(full_path_project, TEMPLATE_FOLDER, folder, file)
            new_dir = os.path.join(full_path_project, TEMPLATE_FOLDER, folder)
            create_dir(new_dir)
            create_file(new_file)
