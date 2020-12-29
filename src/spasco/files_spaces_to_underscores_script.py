#!/usr/bin/env python

import os
import sys


if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")


def replacing_spaces():
    listdir_before = os.listdir()
    counter = 0
    for file_folder_name in os.listdir():
        if ' ' in file_folder_name:
            counter += 1
            new_name = file_folder_name.replace(' ', '_')
            os.rename(file_folder_name, new_name)
    print(f'{counter} of {len(listdir_before)} files were renamed!')


def main():
    print(f'You are currently within the {repr(os.getcwd())} directory. '
          'All spaces contained within file- and dirnames of this '
          'directory will be replaced by underscores.')
    perm = input('Do you want to continue? [Y/n] ')
    if perm.lower() == 'y' or perm.lower() == '':
        replacing_spaces()
    elif perm.lower() != 'y':
        print('Abort.')


if __name__ == '__main__':
    main()
