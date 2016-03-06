import os
import time as t

def print_directory_contents(sPath):
    dir_array = []
    file_array = []
    for root, directories, filenames in os.walk(sPath):
        for directory in directories:
            dir_array.append(os.path.join(root, directory))
        for filename in filenames:
            file_array.append(os.path.join(root,filename))

    return dir_array, file_array


    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """

p = print_directory_contents('../')

for i in p:
    for n in i:
        print n
        t.sleep(0.5)
