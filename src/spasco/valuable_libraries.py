
import logging

# increase logging level to print info/warnings, format logRecord:
logging.basicConfig(filename='Employee.log', level=logging.DEBUG,
                    format='%(levelname)s | %(message)s | %(asctime)s | %(filename)s | %(process)d')

logging.getLogger('this is a logger')

# print(logging.getLogger('this is a logger'))
# logging.debug(f'a debug msg')
# logging.info(f'a info msg')
# logging.warning(f'a warning msg')
# logging.error(f'a error msg')
# logging.critical(f'a critical msg')


class Employee:
    def __init__(self, name):
        self.name = name

        logging.info(f'created Employee: {self.name}')


emp1 = Employee('Niklas Tiede')
emp2 = Employee('Bert Ronson')


# 1. idee: logging in spasco nutzen -> neu generierte dateien werden im logging-datei gespeichert!
# versuchen logging statt print statements einzubauen? es gibt einige print statements die ich am
# liebsten immer behalten wollte!

# most often used functions:
import functools
# module is for higher-order functions: functions that act on or return other functions
functools.partial()
functools.wraps()
functools.reduce()

import shutil
# high-level operations on files and collections of files
shutil.rmtree()
shutil.copy()
shutil.copyfile()
shutil.move()
shutil.copytree()

import os
os.makedirs()
os.listdir()
os.environ()
os.remove()
os.getcwd()
os.mkdir()
# os.path.
os.walk()
os.system()
os.chdir()
os.stat()
os.rename()
os.name()
os.chmod()
os.access()

import sys
sys.argv()
sys.exit()
sys.version_info()
sys.path()
sys.stdout()
sys.stderr()
sys.modules()
sys.platform()

import time
time.time()
time.sleep()
time.strftime()
time.localtime()

import json
json.loads()
json.dumps()
json.load()
json.dump()

import argparse
argparse.ArgumentParser()

import collections
collections.OrderedDict()
collections.defaultdict()
collections.namedtuple()
collections.Counter()
collections.deque()

import random
random.randint()
random.choice()
random.random()
random.shuffle()
random.seed()
random.sample()
random.randrange()
random.uniform()

import logging
logging.getLogger()
logging.INFO
logging.DEBUG
logging.basicConfig()
logging.StreamHandler()
logging.Formatter()
logging.info()
logging.FileHandler()
logging.WARNING
logging.ERROR
logging.debug()
logging.error()
logging.warning()

import datetime
datetime.timedelta()
datetime.datetime()
datetime.date()

import subprocess
subprocess.Popen()
subprocess.PIPE
subprocess.check_output()
subprocess.call()
subprocess.CalledProcessError()
subprocess.STDOUT
subprocess.check_call()
subprocess.run()

import copy
# shallow and deep copy
copy.deepcopy()
copy.copy()

import itertools
itertools.chain()
itertools.product()
itertools.islice()

import threading
threading.Thread()
threading.Lock()
threading.Event()

import io
# text I/O, binary I/O and raw I/O
# concrete object belonging to any of these categories is called a file object.
# Other common terms are stream and file-like object
io.BytesIO()
io.StringIO()
io.open()

import glob
# finds all the pathnames matching a specified pattern according
# to the rules used by the Unix shell
glob.glob()

import pytest
pytest.raises()
pytest.fixture()

import hashlib
#  interface to many different secure hash and message digest algorithms
hashlib.md5()
hashlib.sha256()

import warnings
#  For example, one might want to issue a warning when a program uses an obsolete module
warnings.warn()
warnings.simplefilter()
warnings.filterwarnings()
warnings.catch_warnings()

import socket
# low level networking interface
socket.socket()

import traceback
# module provides a standard interface to extract, format and print stack
# traces of Python programs. It exactly mimics the behavior of the Python
# interpreter when it prints a stack trace. This is useful when you want
# to print stack traces under program control, such as in a “wrapper” around
# the interpreter
traceback.format_exc()
traceback.print_exc()

import string
string.digits()
string.ascii_letters()
string.ascii_uppercase()
string.ascii_lowercase()
string.punctuation()

import multiprocessing
multiprocessing.Process()
multiprocessing.Pool()
multiprocessing.cpu_count()
multiprocessing.Queue()
multiprocessing.Manager()

import inspect
inspect.isclass()
inspect.getmembers()

import uuid
uuid.uuid4()

import operator  # ??
operator.itemgetter()

import platform
platform.system()
platform.python_version()
platform.machine()
platform.platform()
platform.architecture()

import urllib  # interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.)
urllib.urlencode()
urllib.quote()

import yaml  # pip install pyyaml
yaml.load()
yaml.safe_load()
yaml.dump()

import typing  # to use type hints and function annotations
typing.List()
typing.Optional()
typing.Dict()
typing.Tuple()
typing.Union()

import tqdm
tqdm.tqdm()

import zipfile
zipfile.ZipFile()

import abc
abc.ABCMeta()
abc.abstractmethod()

import pathlib  # path-module is easier to use
pathlib.Path()

import importlib
importlib.import_module()  # vs .__import__()

import pprint
pprint.pprint()
pprint.pformat()  # formatted representation of object as a string

import gzip  # interface to compress and decompress files just like the GNU programs gzip and gunzip would
gzip.open()
gzip.GzipFile()
gzip.decompress()
gzip.compress()

import configparser    # end user can configure program easily
configparser.ConfigParser()
