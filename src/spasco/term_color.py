# Colorize your terminal output !

# You can also just copy the code below (Txt and fmt()) 
# to avoid yet another dependancy in your project !

# terminals other than the linux standard terminal can display colors differently..

class Txt:
    """ ANSI codes of colors """
    red = '\033[31m'
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
    """ terminal output of a string can be colorized, bolded or underlined. The
    colors are stored within the Txt-class. """

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


def show_all_colors(your_string='colorized font'):
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
        'white'
    ]

    all_colors = ''
    for color in rainbow:
        textcolor = eval(f'Txt.{color}')
        colorname = ' '*(9-len(color)) + color
        colorname = fmt(text=colorname, textcolor=textcolor)
        normal_color = fmt(text=your_string, textcolor=textcolor)
        bolded_color = fmt(text=your_string, textcolor=textcolor, bolded=True)
        underlined_color = fmt(text=your_string, textcolor=textcolor, underlined=True) 
        bol_undl_color = fmt(text=your_string, textcolor=textcolor, bolded=True, underlined=True)
        line = f"{colorname}:  {normal_color}  {bolded_color}  {underlined_color}  {bol_undl_color}\n"
        all_colors += line
    return all_colors


# example:
# from term_color import Txt, fmt
# some_text = "This is some text I've written."
# print(fmt(some_text, textcolor=Txt.green, bolded=True))


# print(show_fmt())

