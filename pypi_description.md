
Spasco is a glorified replace function: it lets you remove or replace characters occurring in file or directory names. By default it replaces whitespaces by underscores but you can easily customize the characters you want to remove/replace.

# Example

If you have files or directories containing whitespaces in your current working
directory you can easily replace them by underscores using `spasco`:

```console
❯ ls
test dir
test file

❯ spasco
You can rename 2 files and/or directories.

Before           After
──────────────────────────
'test file'  🡆  'test_file'
'test dir'   🡆  'test_dir'
──────────────────────────

❯ OK to proceed with renaming? [y/n] y
All done! 1 files and 1 directories were renamed! ✨💄✨

❯ ls
test_dir
test_file
```

# Features

Spasco's renaming operation can be modified. For example, the
search-value (default: whitespaces) and the new-value (default: underscore) can be
changed.

- Search-values other than whitespaces and new-values other than
  underscores can be selected temporarily or permanently
- Files/directories within directories can be renamed (recurse into directories)
- Scope of the renaming action can be limited (patterns with wildcard
  characters, filename expansion)
- A log of the renaming actions can be recorded


# Configuration

Spasco has a configuration file that allows you to change its default
behaviour. The file is generated automatically when running spasco.

```ini
[VALUE-SETTINGS]
search_value = ' '
new_value = _

[LOG-SETTINGS]
logging_turned_on = False
logger_filename = spasco.log
logger_location = /home/user
```

Configuration is done through the command line interface. Logging can be turned on and off and you can customize the new search-/new-value permanently.

```console
❯ spasco config --help
usage: spasco config [--show-setting] [-o true/false] [-n [filename]] [-l [pathname]] [-h, --help ]

search-value and new-value can be changed. Logging to record all renaming actions as log file can be activated.

optional arguments:
  --show-settings    Returns your current settings for logging and renaming.
  -h, --help         Show this help message and exit.

log settings:
  -o [true/false]    Logging is turned on/off (default: off).
  -f [filename]      Set a new filename for the logger.
  -l [pathname]      Set a new file location for the logger.

renaming settings:
  -s [search_value]  Set a new 'search-value' permanently.
  -n [new_value]     Set a new 'new-value' permanently.
```

# How to use Spasco


The built-in help flag `--help` shows which flags can be used.

```console
optional arguments:
  -t [file_or_dir]     Select a single file or directory for renaming.
  -s [search_value]    Define custom search-value (default: ' ').
  -n [new_value]       Define custom new-value (default: '_').
  -p [pattern_only]    Only files/dirs containing the pattern are renamed.
  -e [except_pattern]  Only files/dirs not containing the pattern are
                       renamed.
  -d, --dirs-only      Only directories are renamed.
  -f, --files-only     Only files are renamed.
  -r, --recursive      Recurse into directories.
  -i, --immediately    Skip security question, renaming preview and execute
                       immediately.
  -v, --version        Show version number and exit.
  -h, --help           Show this help message and exit.

log and renaming configuration:
  config               Sub-command to interact with spasco's logging and
                       rename settings.
```

## Example 1: Removing Characters

To remove characters of a kind you have to define an empty-string new-value. In the following example all dash characters will be removed:

```
❯ spasco -s '-' -n ''
You can rename 2 files and/or directories.

Before          After
────────────────────────
'folder-1'  🡆  'folder1'
'folder-2'  🡆  'folder2'
────────────────────────
```

## Example 2: Limit Renaming to Certain Files

Sometimes nyou don't wanna rename every file. For that case you can include/exclude files containing a specific pattern. If you want to rename only files which contain a pattern use the `-p` flag.

```
❯ spasco -p '*.py'
```

If you want to prevent renaming of a file use the `-e` flag. In the following we exclude all dotfiles from the renaming operation.

```
❯ spasco -e '.*'
```

## Example 3: Set Search/New Values Permanently

You can change search/new-values permamnently by changing spascos configuration. For instance if you plan just to remove characters you can change spasco's default behavior permanently:

```
❯ spasco config -n ''
spasco -s '.py'   #  removes all .py file endings

❯ spasco config --show-settings
value settings:
  search_value: ' '
  new_value: ''
log settings:
  logging_turned_on: False
  logger_filename: spasco.log
  logger_location: /home/niklas
```


## Example 4: Activate Logging

Logging your renaming operations is a useful safety net. If you renamed a file accidentally and you realize later on that you broke something it's nice to know which files where renamed. Logging is turned off by default, but you can turn it on:

```
❯ spasco config -o true
Logging is activated.
```

All renaming operations will be logged in your `HOME` directory within a `spasco.log` file.
