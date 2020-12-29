# """ CLI for spasco """
# # Copyright (c) 2020, Niklas Tiede.
# # All rights reserved. Distributed under the MIT License.
#
# import argparse
# import sys
#
#
# __version__ = "0.1.0"
# __author__ = 'Niklas Tiede'
# __author_email__ = 'niklastiede2@gmail.com'
# __doc_url__ = 'https://feedingorcas.readthedocs.io'
# __src_url__ = 'https://github.com/NiklasTiede/feedingORCAs'
#
# # tutorials for argparse:
# 'https://realpython.com/command-line-interfaces-python-argparse/'
# 'https://docs.python.org/3/howto/argparse.html'
#
#
# def main(argv):
#     """
#     """
#     parser = __build_parser()
#     args = parser.parse_args(argv[1:])
#     print(args)
#
#     if args.version:
#         print(f'spasco {__version__}')
#         return 0
#
#     # if len(sys.argv) < 2:
#     #     parser.print_help()
#     #     sys.exit(0)
#
#     if args.dirsonly:
#         print(args.dirsonly)
#
#
# def __build_parser():
#     """Constructs the parser for the command line arguments.
#
#     :returns
#         An ArgumentParser instance for the CLI.
#     """
#
#     parser = argparse.ArgumentParser(prog='spasco', description='Cheminformatics toolkit.')
#     parser.add_argument('-v',
#                         '--version',
#                         action='version',
#                         version='0.1',
#                         help='show version number and exit')
#     parser.add_argument('-d',
#                         '--dirsonly',
#                         action='store_true',
#                         help='renames only directories')
#     parser.add_argument('-f',
#                         '--filesonly',
#                         action='store_true',
#                         help='renames only files')
#     parser.add_argument('-o',
#                         '--only <*.py>',
#                         action='store_true',
#                         help='renames only files/dirs containing the pattern')
#     parser.add_argument('-e',
#                         '--excluding <*.py>',  # pattern
#                         action='store_true',
#                         help='renames all files/dirs except for files/dirs containing the pattern')
#     parser.add_argument('-s',
#                         '--show',
#                         action='store_true',
#                         help='shows all files/dirs containing whitespaces.')
#     parser.add_argument('-i',
#                         '--input-pattern',
#                         action='store_true',
#                         help='replaces another pattern, not whitespaces')
#     parser.add_argument('-op',
#                         '--output-pattern',
#                         action='store_true',
#                         help='replaces pattern by another pattern, not underscores')
#     return parser
#
#
# def run_main():
#     try:
#         sys.exit(main(sys.argv))
#     except Exception as e:
#         sys.stderr.write('spasco: ' + str(e) + '\n')
#         sys.exit(1)
#
#
# if __name__ == '__main__':
#     run_main()
