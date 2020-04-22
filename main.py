import bz2
import os
import pathlib

dest_folder = "arch"
source_name = "C:\\progs\\ispace\\sdm_python\\sdm-plugin-python"


def zipper(source_name, dir_name):
    for path, subdirs, files in os.walk(f"{source_name}/{dir_name}"):
        if not os.path.exists("./{}/{}".format(dest_folder, path[len(source_name):])):
            os.makedirs("./{}/{}".format(dest_folder, path[len(source_name):]))
        for name in files:
            filename = pathlib.PurePosixPath(path, name)
            print(filename)
            with open(filename, 'rb') as data:
                tarbz2contents = bz2.compress(data.read(), 9)
                fh = open("{}/{}/{}.bz2".format(dest_folder, path[len(source_name):], name), "wb")
                print(path[len(source_name):])
                fh.write(tarbz2contents)
                fh.close()


def zip_files(source_directory, dir_list):
    for dir_name in dir_list:
        zipper(source_directory, dir_name)

# "maps","materials", "models", "sound"
zip_files(source_name, ["sound", "maps", "materials", "models"])
