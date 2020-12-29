

# import term_color
# print(term_color.show_all_colors())



import configparser
config = configparser.ConfigParser()
config.read('settings.ini')

# # create setting.ini using a python script:
# config['YOUR-SETTINGS'] = {
#     'Logging_turned_on': False,
#     'logger_filename': 'spasco.log',
#     'logger_location': os.environ['HOME'],
#     }

# # adding values like in a python dictionary, values have to be quoted to be strings !
# config['YOUR-SETTINGS']['stuff'] = '12'

# with open('settings.ini', 'w') as fp:
#     config.write(fp)

# # ------------------------
#
# # read setting.ini and load kez-value paris:
# config.read("settings.ini")
#
# config.sections('YOUR-SETTINGS')
# config.options('SectionOne')
#
# config.get('SectionOne', 'Status')
#
# config.getboolean('<section>', '<optionname>')
# config.getfloat()
# # config.getint()


# logger_path = f"{config.get('YOUR-SETTINGS', 'logger_location')}/{config.get('YOUR-SETTINGS', 'logger_filename')}"
# print(bool('false'))
# bool_map = {'True': True, 'False': False}
# x = config.getboolean('YOUR-SETTINGS', 'logging_turned_on')
# print(x)

# add tilde/filename expansion using the -f=~/Down with glob

from pprint import pprint
import glob
import os

# pattern = '*.py'
# glob_filter = [name for name in glob.glob(pattern)]
# pprint(glob_filter)
#
# base, file = os.path.split('reefneu/sdfcsndc/fefe.py')
# print(file)

# # --------------------
# exp = '~/Downloads'
# for a in glob.glob('./**'):
#     print(a)

# expand tilde:
inputstr = '~/Downloads.txt'
if '~' in inputstr:
    print('tilde expansion was performed')
    foo = os.path.expanduser(inputstr)
    print(f'{foo!r} a valid dir? {os.path.isdir(foo)}')

# enetered path must be a valid directory!

if '~' in inputstr:
    print('tilde expansion was performed')
else:
    print('else fired')



