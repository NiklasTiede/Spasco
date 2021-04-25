# run tests with 'pytest -s -vvv'
# if a test fails: a folder named 'renaming_tests' might be left as artifact, sometimes must be removed manually
import glob
import os
import pathlib
import shutil

from spasco.main import main


# directories/files which have to be generated for every test:
folders = [
    'folder 1',
    'folder-2',
    'folder 1/folder-11',
    'folder 1/folder 12',
    'folder-2/folder21',
    'folder-2/folder22',
]
files = [
    'file 1.py',
    'file-2.js',
    'folder 1/file 11.py',
    'folder 1/file-12.js',
    'folder-2/file 21.py',
    'folder-2/file-22.js',
]

test_location = 'renaming_tests'
os.chdir('tests')
tests_folder = os.getcwd()


def create_test_files_and_dirs():
    # os.chdir('tests')
    if not os.path.exists(test_location):
        os.mkdir(test_location)
    os.chdir(test_location)
    for dirname in folders:
        if not os.path.exists(dirname):
            os.mkdir(dirname)
    for filename in files:
        if not os.path.exists(filename):
            pathlib.Path(filename).touch()


def listdir_recursively():
    """ Returns a list of all files/directories of within the current working directory
    recursively. This function is like 'os.listdir()' but also recursing into directories!
    """
    files_and_dirs = []
    for pathname in glob.iglob(os.getcwd() + '**/**', recursive=True):
        files_and_dirs.append(os.path.relpath(pathname, os.getcwd()))
    sorted_files_and_dirs = sorted(files_and_dirs[1:])
    return sorted_files_and_dirs


#######################################################################
# Test 1: no flags (-i has to be used, to skip the safety question)

expected_filesdirs_without_flags = [
    'file-2.js',
    'file_1.py',             # renamed
    'folder-2',
    'folder-2/file 21.py',
    'folder-2/file-22.js',
    'folder-2/folder21',
    'folder-2/folder22',
    'folder_1',              # renamed
    'folder_1/file 11.py',
    'folder_1/file-12.js',
    'folder_1/folder 12',
    'folder_1/folder-11',
]


def test_renaming_without_flags(capsys):
    """ Tests if the default renaming is functional:
    ' ' to '_' of all files/dirs within current directory.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_filesdirs_without_flags

    # # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 1 files and 1 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


###################################################################
# Test 2: rescursive (-r) flag

expected_files_dirs_with_recursive_flag = [
    'file-2.js',
    'file_1.py',             # renamed
    'folder-2',
    'folder-2/file-22.js',
    'folder-2/file_21.py',   # renamed
    'folder-2/folder21',
    'folder-2/folder22',
    'folder_1',              # renamed
    'folder_1/file-12.js',
    'folder_1/file_11.py',   # renamed
    'folder_1/folder-11',
    'folder_1/folder_12',    # renamed
]


def test_renaming_with_recursive_flag(capsys):
    """ Tests if the recursive flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-r'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_recursive_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 3 files and 2 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)

###################################################################
# Test 3: files-only (-f) flag


expected_files_dirs_with_filesonly_flag = [
    'file-2.js',
    'file_1.py',            # renamed
    'folder 1',
    'folder 1/file 11.py',
    'folder 1/file-12.js',
    'folder 1/folder 12',
    'folder 1/folder-11',
    'folder-2',
    'folder-2/file 21.py',
    'folder-2/file-22.js',
    'folder-2/folder21',
    'folder-2/folder22',
]


def test_renaming_with_filesonly_flag(capsys):
    """ Tests if the files-only flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-f'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_filesonly_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 1 files and 0 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


###################################################################
# Test 4: dirs-only (-d) flag

expected_files_dirs_with_dirsonly_flag = [
    'file 1.py',
    'file-2.js',
    'folder-2',
    'folder-2/file 21.py',
    'folder-2/file-22.js',
    'folder-2/folder21',
    'folder-2/folder22',
    'folder_1',              # renamed
    'folder_1/file 11.py',
    'folder_1/file-12.js',
    'folder_1/folder 12',
    'folder_1/folder-11'
]


def test_renaming_with_dirsonly_flag(capsys):
    """ Tests if the dirs-only flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-d'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_dirsonly_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 0 files and 1 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


###################################################################
# Test 5: select one target (-t) flag

expected_files_dirs_with_singletarget_flag = [
    'file 1.py',
    'file-2.js',
    'folder 1',
    'folder 1/file 11.py',
    'folder 1/file-12.js',
    'folder 1/folder 12',
    'folder 1/folder-11',
    'folder-2',
    'folder-2/file-22.js',
    'folder-2/file_21.py',   # renamed
    'folder-2/folder21',
    'folder-2/folder22'
]


def test_renaming_with_singletarget_flag(capsys):
    """ Tests if the singletarget flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-t', 'folder-2/file 21.py'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_singletarget_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 1 files and 0 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


###################################################################
# Test 6: patternonly (-p) flag

expected_files_dirs_with_patternonly_flag = [
    'file-2.js',            # renamed
    'file_1.py',
    'folder 1',
    'folder 1/file-12.js',
    'folder 1/file_11.py',  # renamed
    'folder 1/folder 12',
    'folder 1/folder-11',
    'folder-2',
    'folder-2/file-22.js',
    'folder-2/file_21.py',  # renamed
    'folder-2/folder21',
    'folder-2/folder22'
]


def test_renaming_with_patternonly_flag(capsys):
    """ Tests if the patternonly flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-r', '-p', '*.py'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_patternonly_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 3 files and 0 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


###################################################################
# Test 6: exceptpattern (-p) flag

expected_files_dirs_with_exceptpattern_flag = [
    'file 1.py',
    'file-2.js',
    'folder-2',
    'folder-2/file 21.py',
    'folder-2/file-22.js',
    'folder-2/folder21',
    'folder-2/folder22',
    'folder_1',            # renamed
    'folder_1/file 11.py',
    'folder_1/file-12.js',
    'folder_1/folder-11',
    'folder_1/folder_12'   # renamed
]


def test_renaming_with_exceptpattern_flag(capsys):
    """ Tests if the exceptpattern flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-r', '-e', '*.py'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_exceptpattern_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 0 files and 2 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)

###################################################################
# Test 7: searchvalue (-s) flag


expected_files_dirs_with_searchvalue_flag = [
    'file 1.py',
    'file_2.js',           # renamed
    'folder 1',
    'folder 1/file 11.py',
    'folder 1/file_12.js',  # renamed
    'folder 1/folder 12',
    'folder 1/folder_11',  # renamed
    'folder_2',            # renamed
    'folder_2/file 21.py',
    'folder_2/file_22.js',  # renamed
    'folder_2/folder21',
    'folder_2/folder22'
]


def test_renaming_with_searchvalue_flag(capsys):
    """ Tests if the searchvalue flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-r', '-s', '-'])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_searchvalue_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 3 files and 2 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


###################################################################
# Test 8: newvalue (-n) flag

expected_files_dirs_with_newvalue_flag = [
    'file-2.js',
    'file1.py',
    'folder-2',
    'folder-2/file-22.js',
    'folder-2/file21.py',
    'folder-2/folder21',
    'folder-2/folder22',
    'folder1',
    'folder1/file-12.js',
    'folder1/file11.py',
    'folder1/folder-11',
    'folder1/folder12'
]


def test_renaming_with_newvalue_flag(capsys):
    """ Tests if the searchvalue flag is functional.
    """
    # generate folder/files for renaming test
    create_test_files_and_dirs()

    # renaming operation
    main(['dummy', '-i', '-r', '-n', ''])

    resulting_filesdirs = listdir_recursively()
    assert resulting_filesdirs == expected_files_dirs_with_newvalue_flag

    # compare the generated output message of spasco to the expected message:
    captured_statement = capsys.readouterr().out
    expected_statement = '\033[36mAll done! 3 files and 2 directories were renamed! ✨💄✨\033[0m\n'
    assert captured_statement == expected_statement

    # remove all generated folders/files:
    os.chdir(tests_folder)
    if os.path.exists(test_location):
        shutil.rmtree(test_location)


######################################################################
# deleting test-files/dirs even if a test failed:
os.chdir(tests_folder)
if os.path.exists(test_location):
    shutil.rmtree(test_location)
