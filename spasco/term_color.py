"""terminal color
==============
module for coloring the terminal output
"""
# Copyright (c) 2020, Niklas Tiede.
# All rights reserved. Distributed under the MIT License.


class Txt:
    """ ANSI codes for text colors and formatting (bold, underline). """
    red: str = '\033[31m'
    orange = '\033[91m'
    yellow = '\033[33m'
    green = '\033[32m'
    greenblue = '\033[36m'
    blue = '\033[34m'
    purple = '\033[95m'
    pink = '\033[35m'
    white = '\033[37m'
    black = '\033[30m'


def fmt(text: str, textcolor: str = '', bolded: bool = False, underlined: bool = False) -> str:
    """ the terminal output can be colorized, bolded or underlined.
    Colors are stored within the Txt-class.
    :argument
      text: string which should be formatted
      textcolor (optional): a property of the Txt-class determines the color

    :returns
      string wrapped with ANSI-code.
    """

    bold_str = '\033[1m'
    underline_str = '\033[4m'
    end = '\033[0m'

    if bolded and underlined:
        return f"{textcolor}{underline_str}{bold_str}{text}{end}"
    if bolded:
        return f"{textcolor}{bold_str}{text}{end}"
    if underlined:
        return f"{textcolor}{underline_str}{text}{end}"
    return f"{textcolor}{text}{end}"


def show_all_colors(your_string: str = 'colorized font') -> str:
    """ print out all forms of formatting. """

    rainbow = [
        'pink',
        'red',
        'orange',
        'yellow',
        'green',
        'greenblue',
        'blue',
        'purple',
        'black',
        'white',
    ]

    all_colors = ''
    for color in rainbow:
        textcolor = eval(f'Txt.{color}')
        colorname = ' ' * (9 - len(color)) + color
        colorname = fmt(text=colorname, textcolor=textcolor)
        normal_color = fmt(text=your_string, textcolor=textcolor)
        bolded_color = fmt(text=your_string, textcolor=textcolor, bolded=True)
        underlined_color = fmt(text=your_string, textcolor=textcolor, underlined=True,)
        bol_undl_color = fmt(text=your_string, textcolor=textcolor, bolded=True, underlined=True,)
        line = f"{colorname}:  {normal_color}  {bolded_color}  {underlined_color}  {bol_undl_color}\n"
        all_colors += line
    return all_colors


# # example (How to use when coloring strings):
# from term_color import Txt, fmt
# some_text = "This is some text I've written."
# print(fmt(some_text, textcolor=Txt.green, bolded=True))


def main() -> None:
    print(show_all_colors())


if __name__ == '__main__':
    main()
