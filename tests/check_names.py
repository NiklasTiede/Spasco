# this scripts returns an arrays of all files/dirs contained within the 'renaming_tests' folder
# to confirm the hardcoded results of spasco's renaming operation
import glob
import os
from pprint import pprint


def listdir_recursively():
    """ Returns a list of all files/directories of within the current working directory
    recursively. This function is like 'os.listdir()' but also recursing into directories!
    """
    files_and_dirs = []
    for pathname in glob.iglob(os.getcwd() + '**/**', recursive=True):
        files_and_dirs.append(os.path.relpath(pathname, os.getcwd()))
    sorted_files_and_dirs = sorted(files_and_dirs[1:])
    return sorted_files_and_dirs


os.chdir('tests/renaming_tests')
x = listdir_recursively()
pprint(x)
