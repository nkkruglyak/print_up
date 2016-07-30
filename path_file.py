import os
def del_files(path_dir):
    path = os.path.abspath(path_dir)
    list_files = os.listdir(path_dir)
    for file in list_files:
        full_path = os.path.join(path, file)
        os.remove(full_path)

