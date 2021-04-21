"""spasco - spaces to underscores
==============================
command line tool for replacing spaces within files and directories
"""
# Copyright (c) 2020, Niklas Tiede.
# All rights reserved. Distributed under the MIT License.
import argparse
import configparser
import fnmatch
import logging
import os
import sys
from argparse import _SubParsersAction
from argparse import ArgumentParser
from argparse import HelpFormatter
from pprint import pprint
from typing import List

from spasco import __src_url__, __title__, __version__
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


# set a logger
# TODO: log each renamed path
logger_path = f"{config.get('LOG-SETTINGS', 'logger_location')}/{config.get('LOG-SETTINGS', 'logger_filename')}"
logging.basicConfig(
    filename=logger_path,
    level=logging.INFO,
    format='%(levelname)s | %(asctime)s | %(message)s',
)


if sys.platform != 'linux':
    print(f"{__title__!r} is currently not optimized for Windows / OS X")
    sys.exit(1)


def main(argv):
    """ Main program.

    :argument
        argv: command-line arguments, such as sys.argv (including the program name
        in argv[0]).

    :return
        Zero on successful program termination, non-zero otherwise.
    """

    # parser = __build_parser()[0]
    # args = parser.parse_args(argv[1:])

    main_parser, config_subparser = __build_parser()

    argv = argv[1:]
    
    args = main_parser.parse_args(args=argv)

    # logging.debug(vars(args))

    # triggering config subparser
    if vars(args).get('command', None) == 'config':
        execute_config(config_subparser, argv)
        return 0

    #######################
    # 1 select/sort paths #
    #######################

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
    logging.debug(f'selected list before 1st filter: {files_dirs}')
    all_selected_files_dirs = files_dirs.copy()
    logging.debug(f'number of all files/dirs: {len(all_selected_files_dirs)}')

    # ------ search-value filter ------
    [
        files_dirs.remove(x)
        for x in all_selected_files_dirs if not SEARCH_VALUE in x.split('/')[-1]
    ]
    if not files_dirs:
        print(
            f'None of the selected {len(all_selected_files_dirs)} files/dirs contained the search-value {SEARCH_VALUE!r} ',
        )
        return 1
    logging.debug(
        f'selected list after 1st filter (search-value): {files_dirs}',
    )

    # ------ pattern-only filter ------
    [
        files_dirs.remove(x) for x in files_dirs.copy() if args.pattern_only and
        not fnmatch.fnmatch(os.path.split(x)[1], args.pattern_only)
    ]
    if not files_dirs:
        print(
            f'No file/dir present containing the pattern {args.pattern_only!r} ',
        )
        return 1
    logging.debug(
        f'selected list after 2nd filter (pattern-only): {files_dirs}',
    )

    # ------ except-pattern filter -----
    [
        files_dirs.remove(x) for x in files_dirs.copy() if args.pattern_only and
        fnmatch.fnmatch(os.path.split(x)[1], args.pattern_only)
    ]
    if not files_dirs:
        print(
            f'No file/dir present containing the search-value {SEARCH_VALUE!r} and not the except-pattern {args.except_pattern!r} ',
        )
        return 1
    logging.debug(
        f'selected list after 3rd filter (except-pattern): {files_dirs}',
    )

    # ------ dirs-only filter -----
    [
        files_dirs.remove(x) for x in files_dirs.copy()
        if args.dirs_only and not os.path.isdir(x)
    ]
    if not files_dirs:
        print(f'No directory present after filtering out files.')
        return 1
    logging.debug(f'selected list after 4th filter (dirs-only): {files_dirs}')

    # ------ files-only filter -----
    [
        files_dirs.remove(x) for x in files_dirs.copy() if args.files_only and
        not os.path.isfile(x)
    ]
    if not files_dirs:
        print(f'No file present after filtering out directories.')
        return 1
    logging.debug(f'selected list after 5th filter (files-only): {files_dirs}')
    filtered_paths = files_dirs

    ################
    #  3 renaming  #
    ################

    NEW_VALUE = args.new_value if args.new_value else config.get(
        'VALUE-SETTINGS', 'new_value',
    )

    renamed_paths = path_renaming(
        path_lst=filtered_paths,
        search_value=SEARCH_VALUE,
        new_value=NEW_VALUE,
    )

    # print(f'{len(filtered_paths)} files/directories can be renamed:')
    # print(f"before {' ' * (max([len(x) for x in filtered_paths]) - len('before') + 6)} after",)
    # for before, after in list(zip(filtered_paths, renamed_paths)):
    #     print(f"{before!r}{' ' * (max([len(x) for x in filtered_paths]) - len(before))} --> {after!r}",)


    if args.immediately:
        is_proceeding = 'y'
    else:
        print(f'{len(filtered_paths)} files/directories can be renamed:')
        print(f"before {' ' * (max([len(x) for x in filtered_paths]) - len('before') + 6)} after",)
        for before, after in list(zip(filtered_paths, renamed_paths)):
            print(f"{before!r}{' ' * (max([len(x) for x in filtered_paths]) - len(before))} --> {after!r}",)

        is_proceeding = input('OK to proceed with renaming? [y/n] ')


    if is_proceeding.lower() == 'y':
        new_pathnames = path_renaming(
            path_lst=filtered_paths, search_value=SEARCH_VALUE, new_value=NEW_VALUE, renaming=True,
        )
        filecount, dircount = 0, 0

        for path in new_pathnames:
            # fullpath = os.getcwd() + '/' + path
            # print(fullpath)
            if os.path.isdir(path):
                # print(fullpath)
                dircount += 1
            if os.path.isfile(path):
                # print(fullpath)
                filecount += 1
        print(f'All done! {filecount} files and {dircount} directories were renamed ✨ 🍰 ✨.')
        return 0
    else:
        print(fmt("command aborted.", textcolor=Txt.greenblue))
        return 1


def execute_config(config_subparser, argv):
    """ subparser triggering from main is refactored in here. """

    args = config_subparser.parse_args(argv[1:])

    if args.show_settings:
        print(f'{fmt("value settings:", Txt.greenblue)}')
        print(
            f"  search_value: {config.get('VALUE-SETTINGS', 'search_value')}",
        )
        print(f"  new_value: {config.get('VALUE-SETTINGS', 'new_value')}")
        print(f'{fmt("log settings:", Txt.greenblue)}')
        print(
            f"  logging_turned_on: {config.getboolean('LOG-SETTINGS', 'logging_turned_on')}",
        )
        print(
            f"  logger_filename: {config.get('LOG-SETTINGS', 'logger_filename')}",
        )
        print(
            f"  logger_location: {config.get('LOG-SETTINGS', 'logger_location')}",
        )
        return 0

    if args.turn_log_on:
        print(f'change logging on/off: {args.turn_log_on.capitalize()}')
        config['LOG-SETTINGS']['logging_turned_on'] = args.turn_log_on.capitalize()
        with open(settings_file, 'w') as fp:
            config.write(fp)
        log_state = config.getboolean('LOG-SETTINGS', 'logging_turned_on')
        if log_state:
            print('log recording is activated.')
        else:
            print('log recording is deactivated.')
        return 0

    if args.log_name:
        config['LOG-SETTINGS']['logger_filename'] = args.log_name
        with open(settings_file, 'w') as fp:
            config.write(fp)
        print(
            f"The new log filename is {config.get('LOG-SETTINGS', 'logger_filename')}",
        )
        return 0

    if args.log_location:
        log_location = args.log_location
        if '~' in args.log_location:
            log_location = os.path.expanduser(args.log_location)
        if not os.path.isdir(log_location):
            print(
                f'The given path {args.log_location!r} is not a valid directory!',
            )
            return 1
        config['LOG-SETTINGS']['logger_location'] = log_location
        with open(settings_file, 'w') as fp:
            config.write(fp)
        print(
            f"The new log location is {config.get('LOG-SETTINGS', 'logger_location')}",
        )
        return 0

    if args.set_search_value:
        config['VALUE-SETTINGS']['search_value'] = args.set_search_value
        with open(settings_file, 'w') as fp:
            config.write(fp)
        print(
            f"The new search-value is {config.get('VALUE-SETTINGS', 'search_value')}",
        )
        return 0

    if args.set_new_value:
        config['VALUE-SETTINGS']['new_value'] = args.set_new_value
        with open(settings_file, 'w') as fp:
            config.write(fp)
        print(
            f"The new 'new-value' is {config.get('VALUE-SETTINGS', 'new_value')}",
        )
        return 0

    config_subparser.print_help()
    return 1


def path_renaming(path_lst: List[str], search_value: str, new_value: str, renaming: bool = False) -> List[str]:
    """ names if renamed paths are returned and they can be  """
    renamed_paths = []
    for old_path_name in path_lst:
        resulting_name = old_path_name.replace(search_value, new_value)
        renamed_paths.append(resulting_name)
        path_base, file = os.path.split(old_path_name)
        new_name = file.replace(search_value, new_value)
        full_new = os.path.join(path_base, new_name)
        if renaming:
            os.rename(old_path_name, full_new)
            logging.info(
                f" working dir: {os.getcwd()!r} | naming: {old_path_name!r} --> {full_new!r}",
            )
    return renamed_paths


def recurse_dirs_and_files() -> List[str]:
    """ all directories and files
    :returns
        all dirs and files recursive, sorted
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
            # print('rel. dirpath:', rel_dirpath.split('/'))
            all_files_dirs.append(rel_dirpath)
    return all_files_dirs


# hack for removing the metavar below the subparsers title


class NoSubparsersMetavarFormatter(HelpFormatter):
    def _format_action(self, action):
        result = super()._format_action(action)
        if isinstance(action, _SubParsersAction):
            # fix indentation on first line
            return "%*s%s" % (self._current_indent, "", result.lstrip())
        return result

    def _format_action_invocation(self, action):
        if isinstance(action, _SubParsersAction):
            # remove metavar and help line
            return ""
        return super()._format_action_invocation(action)

    def _iter_indented_subactions(self, action):
        if isinstance(action, _SubParsersAction):
            try:
                get_subactions = action._get_subactions
            except AttributeError:
                pass
            else:
                # remove indentation
                yield from get_subactions()
        else:
            yield from super()._iter_indented_subactions(action)


class MyOwnFormatter(NoSubparsersMetavarFormatter, argparse.RawDescriptionHelpFormatter):
    """ removes metavar of config subparser and adds RawDescription """
    pass


def __build_parser():
    """Constructs the main_parser for the command line arguments.

    :returns
      An ArgumentParser instance for the CLI.
    """
    # noinspection PyTypeChecker
    main_parser = argparse.ArgumentParser(
        prog=__title__,
        add_help=False,
        description=f'A renaming tool which replaces whitespaces within file- or directory names '
                    f'by underscores. By default all files/dirs within the current working '
                    f'directory are renamed.\n\nsrc: {__src_url__}',
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
        help='Searches for characters/patterns to be replaced other than whitespaces.',
    )
    main_parser.add_argument(
        '-n',
        dest='new_value',
        nargs='?',
        action='store',
        metavar='new_value',
        help='Substitutes the search-value for custom characters/patterns other than underscores.',
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
        help='Skip security question and execute immediately.',
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
        title='log and rename configuration',
    )
    config_subparser = add_config_subparser(config_subparsers)
    return main_parser, config_subparser


def add_config_subparser(sub_parsers):
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
        help="Log record is turned on/off.",
    )
    config_subparser_logging.add_argument(
        '-f',
        nargs='?',
        metavar='filename',
        dest='log_name',
        help='Set up a new filename for the logger.',
    )
    config_subparser_logging.add_argument(
        '-l',
        nargs='?',
        metavar='pathname',
        dest='log_location',
        help=f'Set up a new file location for the logger.',
    )

    config_subparser_renaming = config_subparser.add_argument_group(
        'rename settings',
    )
    config_subparser_renaming.add_argument(
        '-s',
        nargs='?',
        metavar='search_value',
        dest='set_search_value',
        help=f"Set up a new search value.",
    )
    config_subparser_renaming.add_argument(
        '-n',
        nargs='?',
        metavar='new_value',
        dest='set_new_value',
        help='Set up a new value which will replace the search-value.',
    )

    config_subparser.set_defaults(command='config')
    return config_subparser


def add_parser_help(parser):
    """
    So we can use consistent capitalization and periods in the help. You must
    use the add_help=False argument to ArgumentParser or add_parser to use
    this. Add this first to be consistent with the default argparse output.
    """

    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help="Show this help message and exit.",
    )


def run_main():
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        sys.stderr.write(__title__ + ': ' + str(e) + '\n')
        sys.exit(1)


if __name__ == '__main__':
    run_main()
