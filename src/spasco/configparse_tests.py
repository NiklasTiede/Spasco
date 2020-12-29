import configparser
import os

config = configparser.ConfigParser()

# create setting.ini using a python script:
config['YOUR-SETTINGS'] = {
    'Logging_turned_on': False,
    'logger_filename': 'spasco.log',
    'logger_location': os.environ['HOME'],
    }

# # adding values like in a python dictionary, values have to be quoted to be strings !
# config['YOUR-SETTINGS']['stuff'] = '12'

with open('settings.ini', 'w') as fp:
    config.write(fp)


# ------------------------



# read setting.ini and load kez-value paris:
config.read("settings.ini")

# config.section('YOUR-SETTINGS')
# config.options('YOUR-SETTINGS')

# retrieve values from config file:
logging_turned_on = config.getboolean('YOUR-SETTINGS', 'logging_turned_on')
logger_filename = config.get('YOUR-SETTINGS', 'logger_filename')
logger_location = config.get('YOUR-SETTINGS', 'logger_location')

print(f'{logger_location}/{logger_filename}')
with open(f'{logger_location}/{logger_filename}') as fp:
    # write logging, but how?
    pass


# change values in config file:
config['YOUR-SETTINGS']['logging_turned_on'] = ''
config['YOUR-SETTINGS']['logger_filename'] = ''
config['YOUR-SETTINGS']['logger_location'] = ''










