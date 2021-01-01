spasco
=============
spaces-to-underscores

<h1 align="center" style="color: #00918f">  <span style="color: #4176cc">spa</span>ces-to-under<span style="color: #4176cc">sco</span>res</h1>


<p align="center" style="color: #00918f">
    text <br>
    spasco   <br>
    <span style="color: #4176cc">spa</span>ces-to-under<span style="color: #4176cc">sco</span>res
  <br><br>
</p>

<p align="center">
    text
  <br><br>
  <img src="http://s.4cdn.org/image/title/105.gif">
</p>

<div contenteditable>
    <center>
        <span style="color: #00918f">spa</span>ces-to-under<span style="color: #4176cc">sco</span>res
    </center>
</div>

<ins>text</ins>

[comment]: <> (<p style="color:#FF0000">spa</p>)

[comment]: <> (<p style="color:#FF0000">sco</p>)

[comment]: <> (pypi, versions and link to pypi)
[comment]: <> ([![conda version]&#40;https://img.shields.io/&#41;]&#40;https://anaconda.org/&#41;    # https://shields.io/category/version)

[comment]: <> ([![platform]&#40;https://img.shields.io/&#41;]&#40;&#41;    # https://shields.io/category/platform-support)

[comment]: <> ([![license]&#40;https://img.shields.io/conda/&#41;]&#40;&#41;    # https://shields.io/category/license)


[comment]: <> ([![Travis CI]&#40;https://img.shields.io/&#41;]&#40;https://travis-ci.com/github/numpy/numpy&#41;     # https://shields.io/category/build)

[comment]: <> ([![codecov]&#40;https://img.shields.io/&#41;]&#40;https://codecov.io/&#41;    # https://shields.io/category/coverage)

[comment]: <> ([![codacy]&#40;https://img.shields.io/&#41;]&#40;&#41;    # https://shields.io/category/analysis)

[comment]: <> (![total lines]&#40;https://img.shields.io/&#41;    # https://shields.io/category/size)

[comment]: <> (![repo size]&#40;https://img.shields.io/&#41;    # https://shields.io/category/size)

Features
--------

spasco let's you replace spaces within a files- or directories name into underscores.

[comment]: <> (gif or animation which shows how spasco works)

Installation
------------

spasco supports several python-versions and is easily installed using pip:

``` {.sourceCode .bash}
pip install spasco
```

text

Tutorial
--------

explaining the most important functionality and more


- [ ] Checkbox off
- [x] Checkbox on

## Features

- Item 1
- Item 2

--------

`code`

    4 space indent
    makes a code block

```
code fences
```


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

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.


```python
your_dict = {
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```


syntax highlighting: yaml, python, html, ini, json

```ini
[VALUE-SETTINGS]
search_value = ' '
new_value = _

[LOG-SETTINGS]
logging_turned_on = False
logger_filename = spasco.log
logger_location = /home/niklas
```


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









