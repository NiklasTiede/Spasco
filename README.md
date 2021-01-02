[comment]: <> (<h1 align="center"> Spasco </h1>)


[comment]: <> (<img align="center" height="150" src="spasco_heading.png" />)

[comment]: <> (<img title="a title" alt="Alt text" src="spasco_heading.png">)
[comment]: <> (   <h3 align="center">Cross-platform dictionary and vocabulary building command line tool</h3> )

<p align="center">
  <img  align="center" height="150" src="spasco_heading.png" />
   <h3 align="center">Cross-platform dictionary and vocabulary building command line tool</h3> 
<p>

[comment]: <> (![pic]&#40;/spasco_heading.png&#41;)



<p align="center">
    <ins>spa</ins>ces-to-under<ins>sco</ins>res
</p>


[comment]: <> ([gif converting file names])


[comment]: <> (# https://shields.io/)

[comment]: <> (![PyPI - Python Version]&#40;https://img.shields.io/pypi/pyversions/spasco&#41;)

[comment]: <> ([![platform]&#40;https://img.shields.io/&#41;]&#40;&#41;    # https://shields.io/category/platform-support)

[comment]: <> ([![license]&#40;https://img.shields.io/conda/&#41;]&#40;&#41;    # https://shields.io/category/license)

[comment]: <> ([![Travis CI]&#40;https://img.shields.io/&#41;]&#40;https://travis-ci.com/github/numpy/numpy&#41;     # https://shields.io/category/build)

[comment]: <> ([![codecov]&#40;https://img.shields.io/&#41;]&#40;https://codecov.io/&#41;    # https://shields.io/category/coverage)

[comment]: <> ([![codacy]&#40;https://img.shields.io/&#41;]&#40;&#41;    # https://shields.io/category/analysis)

[comment]: <> (![total lines]&#40;https://img.shields.io/&#41;    # https://shields.io/category/size)

This tiny command line tool lets you replace whitespaces occurring in file or 
directory names by underscores. Whitespaces are a reserved keyword on the terminal
to separate arguments and thus their usage when naming files/dirs can be problematic.

Example
-------

If you have files or directories containing whitespaces in your current working
directory you can easily replace them by underscores using spasco:

```
❯ ls
test dir
test file

❯ spasco
2 files/directories can be renamed:
before             after
'test dir'  --> 'test_dir'
'test file' --> 'test_file'
OK to proceed with renaming? [y/n] y

❯ ls
test_dir
test_file
```


Table of Contents
-----------------

- [Features](#Features)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [How to use Spasco](#How-to-use-Spasco)


Features
--------

spasco's renaming operation can be modified. For instance the 
search-value (whitespaces) and the new-value (underscores) can be
changed.


- search-values other than whitespaces and new-values other than 
  underscores can be chosen
- files/dirs within directories can be renamed (recurse into dirs)
- scope of the renaming action can be limited (patterns with wildcard 
  characters, filename expansion)
- a log record of the renaming actions can be recorded


Installation
------------

spasco supports several python-versions on linux and is easily 
installed using pip:

``` {.sourceCode .bash}
pip install spasco
```


Configuration
--------

Spasco has a configuration file that allows you to change default 
behaviour. The file is generated automatically when running spasco

. Currently 
tokei looks for this file in three different places. The current 
directory,your home directory, and your configuration directory.

explaining the most important functionality and more

```ini
[VALUE-SETTINGS]
search_value = ' '
new_value = _

[LOG-SETTINGS]
logging_turned_on = False
logger_filename = spasco.log
logger_location = /home/niklas
```

text

```
❯ spasco config --help
usage: spasco config [--show-setting] [-o true/false] [-n [filename]] [-l [pathname]] [-h, --help ]

search-value and new-value can be changed. Logging to record all renaming actions as log file can be activated.

optional arguments:
  --show-settings    Returns your current settings for logging and renaming.
  -h, --help         Show this help message and exit.

log settings:
  -o [true/false]    Log record is turned on/off.
  -f [filename]      Set up a new filename for the logger.
  -l [pathname]      Set up a new file location for the logger.

rename settings:
  -s [search_value]  Set up a new search value.
  -n [new_value]     Set up a new value which will replace the search-value.
```


How to use Spasco
----------------

[comment]: <> (https://github.com/XAMPPRocky/tokei)

text

```bash
ls -la
ls -tree # using lsdeluxe
tree # using tree
```

text


```
❯ spasco --help
usage: spasco [-s [search_value]] [-n [new_value]] [-p [pattern_only]] [-e [except_pattern]] [-d] [-f] [-r] [-v] [-h]
              [files/directories [files/directories ...]] {config} ...

A renaming tool for replacing whitespaces within file- or directory names by underscores.
src: https://github.com/NiklasTiede/spasco

positional arguments:
  files/directories    Select files/dirs to be renamed. Default: current directory is listed.

optional arguments:
  -s [search_value]    Searches for characters/patterns to be replaced other than whitespaces.
  -n [new_value]       substitutes the search-value for custom characters/patterns other than underscores.
  -p [pattern_only]    Only files/dirs containing the pattern are renamed.
  -e [except_pattern]  Only files/dirs not containing the pattern are renamed.
  -d, --dirs-only      Only directories are renamed.
  -f, --files-only     Only files are renamed.
  -r, --recursive      Recurse into directories.
  -v, --version        Show version number and exit.
  -h, --help           Show this help message and exit.

log and rename configuration:
  config               Sub-command to interact with spasco's logging and rename settings.

Make your files more computer-friendly :)
```

text



## Features

- Item 1
- Item 2

--------

`code`

| Column 1 Heading | Column 2 Heading |
| ---------------- | ---------------- |
| Some content     | Other content    |

# h1
## h2
### h3
#### h4
##### h5
###### h6
*italic*
_italic_
**bold**
__bold__

<http://google.com>
[link](http://google.com)

```python
import this
s = "Python syntax highlighting"
for e in [1,2,3]:
    print(e)
```


```python
your_dict = {
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

syntax highlighting: yaml, python, html, ini, json

:bowtie:
:smirk:
:star:
:exclamation:
:grey_exclamation:
:grey_question:
:whale:
:panda_face:
:key:
:lock:
:bulb:
:hammer:
:heavy_check_mark:
