"""spasco - spaces to underscores
==============================
command line tool for replacing/removing whitespaces or other patterns of file- and directory names.
"""
# Copyright (c) 2021, Niklas Tiede.
# All rights reserved. Distributed under the MIT License.
import argparse
import configparser
import fnmatch
import logging
import os
import sys
from argparse import _SubParsersAction
from argparse import HelpFormatter
from typing import List
from typing import Tuple

from spasco import __src_url__
from spasco import __title__
from spasco import __version__
from spasco.term_color import fmt
from spasco.term_color import Txt

base, file = os.path.split(__file__)
settings_file = os.path.join(base, 'settings.ini')

# set up a settings file and then a logger:
config = configparser.ConfigParser()
config.read(settings_file)


# default values for log record are created:
if not config.read(settings_file):
    config['VALUE-SETTINGS'] = {
        'search_value': "' '",
        'new_value': '_',
    }
    config['LOG-SETTINGS'] = {
        'Logging_turned_on': "False",
        'logger_filename': f'{__title__}.log',
        'logger_location': os.environ['HOME'],
    }
    with open(settings_file, 'w') as f:
        config.write(f)


def get_logger_path() -> str:
    logger_location = config.get('LOG-SETTINGS', 'logger_location')
    logger_filename = config.get('LOG-SETTINGS', 'logger_filename')
    return f"{logger_location}/{logger_filename}"


logger_path = get_logger_path()
logging.basicConfig(
    filename=logger_path,
    level=logging.INFO,
    format='%(levelname)s | %(asctime)s | %(message)s',
)


if (sys.platform != 'linux' and sys.platform != 'darwin'):
    print(f"{__title__!r} is currently not optimized for platforms other than OS X / linux")


def main(argv: List[str]) -> int:
    """ Main program.

    :argument
        argv: command-line arguments, such as sys.argv (including the program name
        in argv[0]).

    :return
        Zero on successful program termination, non-zero otherwise.
    """

    main_parser, config_subparser = __build_parser()
    argv = argv[1:]
    args = main_parser.parse_args(args=argv)

    # triggering config subparser
    if vars(args).get('command', None) == 'config':
        execute_config(config_subparser, argv)
        return 0

    ###########################
    # 1 select and sort paths #
    ###########################

    files_dirs = []

    if isinstance(args.file_or_dir, str):
        args.file_or_dir = [args.file_or_dir]

    if args.file_or_dir and not args.recursive:
        files_dirs.extend(args.file_or_dir)

    if args.recursive:
        files_dirs = recurse_dirs_and_files()

    # sort paths (longest paths first) so that renaming starts with the deepest nested file/directory:
    files_dirs = [x.split('/') for x in files_dirs]
    sorted_paths = sorted(files_dirs, key=len, reverse=True)
    files_dirs = ['/'.join(path_as_lst) for path_as_lst in sorted_paths]

    ########################
    #  2: path filtration  #
    ########################

    SEARCH_VALUE = args.search_value if args.search_value else config.get(
        'VALUE-SETTINGS', 'search_value',
    )
    if SEARCH_VALUE == "' '":
        SEARCH_VALUE = ' '

    filtered_paths = []
    all_selected_files_dirs = files_dirs.copy()
    # ------ no file/dir existent ----
    if not files_dirs:
        print('No directory or file present!')
        return 1

    # ------ search-value filter ------
    # [files_dirs.remove(x) for x in all_selected_files_dirs if SEARCH_VALUE not in x.split('/')[-1]]
    for x in all_selected_files_dirs:
        if SEARCH_VALUE not in x.split('/')[-1]:
            files_dirs.remove(x)

    if not files_dirs:
        searchval_msg = f"None of the {len(all_selected_files_dirs)} present files/directories contain the search value '{SEARCH_VALUE}'!"
        print(searchval_msg)
        return 1

    # ------ pattern-only filter ------
    # [files_dirs.remove(x) for x in files_dirs.copy() if args.pattern_only and not fnmatch.fnmatch(os.path.split(x)[1], args.pattern_only)]
    for x in files_dirs.copy():
        if args.pattern_only and not fnmatch.fnmatch(os.path.split(x)[1], args.pattern_only):
            files_dirs.remove(x)

    if not files_dirs:
        print(f'None of the {len(all_selected_files_dirs)} present files/directories contain the pattern {args.pattern_only!r}!')
        return 1

    # ------ except-pattern filter -----
    # [files_dirs.remove(x) for x in files_dirs.copy() if args.except_pattern and fnmatch.fnmatch(os.path.split(x)[-1], args.except_pattern)]
    for x in files_dirs.copy():
        if args.except_pattern and fnmatch.fnmatch(os.path.split(x)[-1], args.except_pattern):
            files_dirs.remove(x)

    if not files_dirs:
        print(f'None of the exception-pattern matching files/directories contain the search-value {SEARCH_VALUE!r}.',)
        return 1

    # ------ dirs-only filter -----
    # [files_dirs.remove(x) for x in files_dirs.copy() if args.dirs_only and not os.path.isdir(x)]
    for x in files_dirs.copy():
        if args.dirs_only and not os.path.isdir(x):
            files_dirs.remove(x)

    if not files_dirs:
        print('No directory present for renaming.')
        return 1

    # ------ files-only filter -----
    # [files_dirs.remove(x) for x in files_dirs.copy() if args.files_only and not os.path.isfile(x)]
    for x in files_dirs.copy():
        if args.files_only and not os.path.isfile(x):
            files_dirs.remove(x)

    if not files_dirs:
        print('No file present for renaming.')
        return 1

    filtered_paths = files_dirs

    ################
    #  3 renaming  #
    ################

    if args.new_value == '':
        NEW_VALUE = ''
    if args.new_value:
        NEW_VALUE = args.new_value
    if args.new_value is None:
        NEW_VALUE = config.get('VALUE-SETTINGS', 'new_value')
        if NEW_VALUE == "''" or NEW_VALUE == '""':
            NEW_VALUE = ''

    filecount, dircount, renamed_paths = path_renaming(
        path_lst=filtered_paths,
        search_value=SEARCH_VALUE,
        new_value=NEW_VALUE,
    )

    if args.immediately:
        is_proceeding = 'y'
    else:
        msg = f'You can rename {len(filtered_paths)} files and/or directories.'  # 🔨
        colored_msg = fmt(msg)  # , Txt.greenblue
        print(colored_msg)
        print()
        before_heading = fmt('Before', Txt.pink, bolded=True)
        after_heading = fmt('After', Txt.blue, bolded=True)
        sep_line = fmt('──', Txt.greenblue)
        print(f"{before_heading} {' ' * (max([len(x) for x in filtered_paths]) - len('before') + 6)} {after_heading}",)
        print(f"{sep_line * (max([len(x) for x in filtered_paths]) + 4)}")
        for before, after in list(zip(filtered_paths, renamed_paths)):
            before_renaming = fmt(before, Txt.pink)
            after_renaming = fmt(after, Txt.blue)
            print(f"'{before_renaming}'{' ' * (max([len(x) for x in filtered_paths]) - len(before))}  {fmt('🡆', Txt.greenblue)}  '{after_renaming}'",)
        print(f"{sep_line * (max([len(x) for x in filtered_paths]) + 4)}")
        print()

        q = fmt(' [y/n] ', Txt.pink)
        proceed_msg = fmt('OK to proceed with renaming?')  # , Txt.greenblue
        is_proceeding = input(proceed_msg + q)

    if is_proceeding.lower() == 'y':
        filecount, dircount, new_pathnames = path_renaming(
            path_lst=filtered_paths,
            search_value=SEARCH_VALUE,
            new_value=NEW_VALUE,
            renaming=True,
        )
        success_msg = fmt(f'All done! {filecount} files and {dircount} directories were renamed! ✨💄✨', Txt.greenblue)
        print(success_msg)
        return 0
    else:
        print(fmt("Command aborted.", textcolor=Txt.pink))
        return 1


settings_msg = f"""{fmt("value settings:", Txt.greenblue)}
  search_value: {config.get('VALUE-SETTINGS', 'search_value')}
  new_value: {config.get('VALUE-SETTINGS', 'new_value')}
{fmt("log settings:", Txt.greenblue)}
  logging_turned_on: {config.getboolean('LOG-SETTINGS', 'logging_turned_on')}
  logger_filename: {config.get('LOG-SETTINGS', 'logger_filename')}
  logger_location: {config.get('LOG-SETTINGS', 'logger_location')}"""


def execute_config(config_subparser: argparse.ArgumentParser, argv: List[str]) -> int:
    """ Boolean logic of config subparser triggering. """

    args = config_subparser.parse_args(argv[1:])

    if args.show_settings:
        print(settings_msg)
        return 0

    if args.turn_log_on:
        config['LOG-SETTINGS']['logging_turned_on'] = args.turn_log_on.capitalize()
        with open(settings_file, 'w') as fp:
            config.write(fp)
        log_state = config.getboolean('LOG-SETTINGS', 'logging_turned_on')
        if log_state:
            print('Logging is activated.')
        else:
            print('Logging is deactivated.')
        return 0

    if args.log_name:
        old_logger_path = get_logger_path()
        config['LOG-SETTINGS']['logger_filename'] = args.log_name
        with open(settings_file, 'w') as fp:
            config.write(fp)
        new_logger_path = get_logger_path()
        os.rename(old_logger_path, new_logger_path)
        print(f"The new log filename is {config.get('LOG-SETTINGS', 'logger_filename')!r}.",)
        return 0

    if args.log_location:
        old_logger_path = get_logger_path()
        log_location = args.log_location
        if '~' in args.log_location:
            log_location = os.path.expanduser(args.log_location)
        if not os.path.isdir(log_location):
            print(f'The given path {args.log_location!r} is not a valid directory!')
            return 1
        config['LOG-SETTINGS']['logger_location'] = log_location
        with open(settings_file, 'w') as fp:
            config.write(fp)
        new_logger_path = get_logger_path()
        os.rename(old_logger_path, new_logger_path)
        print(f"The new log location is {config.get('LOG-SETTINGS', 'logger_location')!r}.",)
        return 0

    if args.set_search_value:
        if args.set_search_value == ' ':
            config['VALUE-SETTINGS']['search_value'] = "' '"
            with open(settings_file, 'w') as fp:
                config.write(fp)
            print(f"The new search-value is {config.get('VALUE-SETTINGS', 'search_value')}.",)
        else:
            config['VALUE-SETTINGS']['search_value'] = args.set_search_value
            with open(settings_file, 'w') as fp:
                config.write(fp)
            print(f"The new search-value is {config.get('VALUE-SETTINGS', 'search_value')!r}.",)
        return 0

    if args.set_new_value == '':
        config['VALUE-SETTINGS']['new_value'] = "''"
        with open(settings_file, 'w') as fp:
            config.write(fp)
        print(f"The new 'new-value' is {config.get('VALUE-SETTINGS', 'new_value')}.")
        return 0

    if args.set_new_value:
        config['VALUE-SETTINGS']['new_value'] = args.set_new_value
        with open(settings_file, 'w') as fp:
            config.write(fp)
        print(f"The new 'new-value' is {config.get('VALUE-SETTINGS', 'new_value')!r}.")
        return 0

    config_subparser.print_help()
    return 1


def path_renaming(path_lst: List[str], search_value: str, new_value: str, renaming: bool = False) -> Tuple[int, int, List[str]]:
    """ List of filtered files and directories are renamed and their names
    returned. Furthermore, the number fo directories/files which were renamed
    are also returned.
    :returns
      Tuples containing the number of directories, files and the names of them after renaming
    """
    renamed_paths = []
    dircount, filecount = 0, 0
    for old_path_name in path_lst:
        path_base, file = os.path.split(old_path_name)
        new_name = file.replace(search_value, new_value)
        full_new = os.path.join(path_base, new_name)
        renamed_paths.append(full_new)
        if renaming:
            os.rename(old_path_name, full_new)
            if os.path.isdir(full_new):
                dircount += 1
            elif os.path.isfile(full_new):
                filecount += 1
            logging.info(f" working dir: {os.getcwd()!r} | naming: {old_path_name!r} --> {full_new!r}",)
    return (filecount, dircount, renamed_paths)


def recurse_dirs_and_files() -> List[str]:
    """ All files/directories within the current working directory are mapped
    into a list.
    :returns
      List of all file/directory paths, recursively and sorted
    """
    all_files_dirs = []
    base_path = os.getcwd()
    # collect all rel. paths in a list (rel to cwd):
    for dirpath, dirnames, filenames in os.walk(base_path):
        for filename in filenames:
            full_filepath = dirpath + '/' + filename
            rel_filepath = os.path.relpath(full_filepath, base_path)
            all_files_dirs.append(rel_filepath)
        for dirname in dirnames:
            full_dirpath = dirpath + '/' + dirname
            rel_dirpath = os.path.relpath(full_dirpath, base_path)
            all_files_dirs.append(rel_dirpath)
    return all_files_dirs


# hack for removing the metavar below the subparsers (config) title
class NoSubparsersMetavarFormatter(HelpFormatter):
    def _format_action_invocation(self, action):  # type: ignore
        if isinstance(action, _SubParsersAction):
            return ""
        return super()._format_action_invocation(action)


class MyOwnFormatter(NoSubparsersMetavarFormatter, argparse.RawDescriptionHelpFormatter):
    """ removes metavar of config subparser and adds RawDescription """
    pass


def __build_parser() -> Tuple[argparse.ArgumentParser, argparse.ArgumentParser]:
    """Constructs the main_parser for the command line arguments.

    :returns
      An ArgumentParser instance for the CLI.
    """
    main_parser = argparse.ArgumentParser(
        prog=__title__,
        add_help=False,
        description=f'Spasco is a glorified replace function. By default it replaces whitespaces\n'
                    f'of all file- and directory names within your current working directory by \n'
                    f'underscores.\n\nsrc: {__src_url__}',
        epilog='Make your files more computer-friendly 😄',
        formatter_class=lambda prog: MyOwnFormatter(
            prog, max_help_position=80,
        ),
    )

    # optional arguments:
    main_parser.add_argument(
        "-t",
        dest='file_or_dir',
        metavar='file_or_dir',
        action='store',
        nargs='?',
        default=os.listdir(),
        help='Select a single file or directory for renaming.',
    )
    main_parser.add_argument(
        '-s',
        dest='search_value',
        nargs='?',
        action='store',
        metavar='search_value',
        help="Define custom search-value (default: ' ').",
    )
    main_parser.add_argument(
        '-n',
        dest='new_value',
        nargs='?',
        action='store',
        metavar='new_value',
        help="Define custom new-value (default: '_')."
    )
    main_parser.add_argument(
        '-p',
        dest='pattern_only',
        nargs='?',
        action='store',
        metavar='pattern_only',
        help='Only files/dirs containing the pattern are renamed.',
    )
    main_parser.add_argument(
        '-e',
        metavar='except_pattern',
        dest='except_pattern',
        nargs='?',
        action='store',
        help='Only files/dirs not containing the pattern are renamed.',
    )
    main_parser.add_argument(
        '-d',
        '--dirs-only',
        action='store_true',
        help='Only directories are renamed.',
    )
    main_parser.add_argument(
        '-f',
        '--files-only',
        action='store_true',
        help='Only files are renamed.',
    )
    main_parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        help='Recurse into directories.',
    )
    main_parser.add_argument(
        '-i',
        '--immediately',
        action='store_true',
        help='Skip security question, renaming preview and execute immediately.',
    )
    main_parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='Show version number and exit.',
        version=f'%(prog)s {__version__}',
    )
    add_parser_help(main_parser)

    # ---- configuration structured as subparser -----
    config_subparsers = main_parser.add_subparsers(
        title='log and renaming configuration',
    )
    config_subparser = add_config_subparser(config_subparsers)
    return main_parser, config_subparser


def add_config_subparser(sub_parsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    """
    """
    config_subparser = sub_parsers.add_parser(
        name='config',
        description='search-value and new-value can be changed. Logging to record all '
                    'renaming actions as log file can be activated.',
        usage=f'{__title__} config [--show-setting] [-o true/false] [-n [filename]] [-l [pathname]] [-h, --help ]',
        add_help=False,
        formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(
            prog, max_help_position=33,
        ),
        help=f"Sub-command to interact with {__title__}'s logging and rename settings.",
    )

    config_subparser.add_argument(
        '--show-settings',
        action='store_true',
        help='Returns your current settings for logging and renaming.',
    )
    add_parser_help(config_subparser)

    config_subparser_logging = config_subparser.add_argument_group(
        'log settings',
    )
    config_subparser_logging.add_argument(
        '-o',
        nargs='?',
        metavar='true/false',
        dest='turn_log_on',
        choices=['true', 'false'],
        help="Logging is turned on/off (default: off).",
    )
    config_subparser_logging.add_argument(
        '-f',
        nargs='?',
        metavar='filename',
        dest='log_name',
        help='Set a new filename for the logger.',
    )
    config_subparser_logging.add_argument(
        '-l',
        nargs='?',
        metavar='pathname',
        dest='log_location',
        help='Set a new file location for the logger.',
    )

    config_subparser_renaming = config_subparser.add_argument_group(
        'renaming settings',
    )
    config_subparser_renaming.add_argument(
        '-s',
        nargs='?',
        metavar='search_value',
        dest='set_search_value',
        help="Set a new 'search-value' permanently.",
    )
    config_subparser_renaming.add_argument(
        '-n',
        nargs='?',
        metavar='new_value',
        dest='set_new_value',
        help="Set a new 'new-value' permanently.",
    )

    config_subparser.set_defaults(command='config')
    return config_subparser


def add_parser_help(parser: argparse.ArgumentParser) -> None:
    """Custom help-argument to have consistent style.
    add_help=False to enable this.
    """
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help="Show this help message and exit.",
    )


def run_main() -> None:
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        sys.stderr.write(__title__ + ': ' + str(e) + '\n')
        sys.exit(1)


if __name__ == '__main__':
    run_main()
