# ~/.config/qutebrowser/themes/base16_default_dark.py

def apply(c):
    # Base colors
    bg  = "#181818"
    fg  = "#d8d8d8"
    red = "#ab4642"
    green = "#a1b56c"
    yellow = "#f7ca88"
    blue = "#7cafc2"
    magenta = "#ba8baf"
    cyan = "#86c1b9"
    bright_black = "#585858"
    bright_white = "#f8f8f8"

    # General UI
    c.colors.completion.fg = fg
    c.colors.completion.category.bg = bg
    c.colors.completion.category.fg = blue
    c.colors.completion.item.selected.bg = bright_black
    c.colors.completion.item.selected.fg = fg

    c.colors.statusbar.normal.bg = bg
    c.colors.statusbar.normal.fg = fg
    c.colors.statusbar.insert.bg = green
    c.colors.statusbar.insert.fg = bg
    c.colors.statusbar.command.bg = bg
    c.colors.statusbar.command.fg = fg

    c.colors.tabs.bar.bg = bg
    c.colors.tabs.odd.bg = bg
    c.colors.tabs.odd.fg = fg
    c.colors.tabs.even.bg = bg
    c.colors.tabs.even.fg = fg
    c.colors.tabs.selected.odd.bg = bright_black
    c.colors.tabs.selected.odd.fg = fg
    c.colors.tabs.selected.even.bg = bright_black
    c.colors.tabs.selected.even.fg = fg

    c.colors.webpage.bg = bg
