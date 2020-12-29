import argparse
import sys
import os

__version__ = "0.1.0"


def main(argv):
    parser = __build_parser()
    args = parser.parse_args(argv[1:])
    print(vars(args))

    # kaboom = vars(args)
    # print(type(kaboom))
    # print(kaboom.values())
    # if kaboom.values():
    #     print('booom')



    # import configparser
    # config = configparser.ConfigParser()
    # config.read('settings.cfg')
    #
    # if args.show_log_settings:
    #     logging_turned_on = config.getboolean('YOUR-SETTINGS', 'logging_turned_on')
    #     logger_filename = config.get('YOUR-SETTINGS', 'logger_filename')
    #     log_location = config.get('YOUR-SETTINGS', 'log_location')
    #     boing = f"""logging_turned_on: {logging_turned_on}\n  logger_filename: {logger_filename}\nlog_file_location: {log_location}"""
    #     print(boing)
    #     return 0

    # if args.file_or_dir:
    #     pass

    # if args.version:
    #     print(f'spasco {__version__}')
    #     return 0

    return 0


def __build_parser():
    # parser = argparse.ArgumentParser(prog='spasco',
    #                                  # usage='%(prog)s [options] path',
    #                                  description='replaces whitespaces by underscores of file- and directory-names.',
    #                                  epilog='make your files more computer-friendly :)',
    #                                  )

    # parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    # # # mutually exclusive groups:
    # # group_a = parser.add_mutually_exclusive_group(required=True)
    # # group_a.add_argument('-v', '--verbose', action='store_true')
    # # group_a.add_argument('-s', '--silent', action='store_true')
    #
    # # positional arguments:
    # parser.add_argument('file_or_dir',
    #                     action='store',
    #                     nargs='*',
    #                     default=os.listdir(),
    #                     # required=True,
    #                     help='renames all files/dirs.')
    #
    # parent_parser = argparse.ArgumentParser(add_help=False)
    # parent_parser.add_argument('--user', '-u',
    #                            default=getpass.getuser(),
    #                            help='username')
    # parent_parser.add_argument('--debug', default=False, required=False,
    #                            action='store_true', dest="debug", help='debug flag')
    # main_parser = argparse.ArgumentParser()
    # service_subparsers = main_parser.add_subparsers(title="service",
    #                                                 dest="service_command")
    # service_parser = service_subparsers.add_parser("first", help="first",
    #                                                parents=[parent_parser])
    # action_subparser = service_parser.add_subparsers(title="action",
    #                                                  dest="action_command")
    # action_parser = action_subparser.add_parser("second", help="second",
    #                                             parents=[parent_parser])
    #
    # config_subparser = parser.add_subparsers()
    #
    # args = main_parser.parse_args()
    #
    #
    #
    # # group args (create subpograms????) TODO
    # group = parser.add_argument_group('configuration')
    # group.add_argument('--foo', help='foo help')
    #
    # # # mutually exclusive groups:
    # # group_a = parser.add_mutually_exclusive_group(required=True)
    # # group_a.add_argument('-v', '--verbose', action='store_true')
    # # group_a.add_argument('-s', '--silent', action='store_true')
    #
    # # optional arguments:
    # parser.add_argument('-p',
    #                     '--pattern-only',
    #                     nargs='?',
    #                     action='store',
    #                     help='renames only files/dirs containing the pattern')
    #
    # parser.add_argument('-v',
    #                     '--version',
    #                     action='store_true',
    #                     help='show version number and exit')

    parser = argparse.ArgumentParser()

    # postiional:
    # parser.add_argument(
    #     'some_args',
    #     action='append',
    #     # nargs='*',
    #     help='More infos.',
    # )

    parser.add_argument(
        'file_or_dir',
        action='store',
        # nargs='*',
        # default=['.'],
        default=os.listdir(),
        help='Renames all files/dirs within the current directory.'
    )

    import configparser
    config = configparser.ConfigParser()
    config.read('settings.cfg')

    group_a = parser.add_mutually_exclusive_group(

        # title='log-configuration',
        # description=None,
    )
    # configparser.getboolean('YOUR-SETTINGS', 'logging_turned_on')
    # configparser.get('YOUR-SETTINGS', 'logger_filename')
    # configparser.get('YOUR-SETTINGS', 'log_location')
    group_a.add_argument(
        '--show-log-settings',
        action='store_true',
        help='Display your current log settings.',
    )
    group_a.add_argument(
        '--activate-log',
        action='store_true',
        help=f'All renaming actions performed by spasco will be logged (within ~/spasco.log).',
    )
    group_a.add_argument(
        '--logger-name',
        action='store',
        help=f"Gives the {config.get('YOUR-SETTINGS', 'logger_filename')}-file a new name.",
    )
    group_a.add_argument(
        '--log-location',
        action='store',
        help=f"Gives the {config.get('YOUR-SETTINGS', 'logger_filename')}-file a new location.",
    )

    # ------------------

    # parser = argparse.ArgumentParser()
    # group1 = parser.add_mutually_exclusive_group(required=True)
    # group1.add_argument('--enable', action='store_true', help='Enable something')
    # group1.add_argument('--disable', action='store_false', help='Disable something')
    # args = parser.parse_args()

    # parser = argparse.ArgumentParser()
    # group1 = parser.add_mutually_exclusive_group()
    # # group1 = mut.add_argument_group(title='required arguments')
    #
    # # group1.add_argument('positional_argument')
    # group1.add_argument('-a', action='store_true')
    # group1.add_argument('-b', action='store_true')
    # # args = parser.parse_args()

    return parser


def run_main():
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        sys.stderr.write('spasco: ' + str(e) + '\n')
        sys.exit(1)


if __name__ == '__main__':
    run_main()
