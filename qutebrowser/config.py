config.load_autoconfig()
config.set("colors.webpage.darkmode.enabled", True)

import os, sys
theme_path = os.path.expanduser("~/.config/qutebrowser/themes/baseTheme.py")
if os.path.exists(theme_path):
    sys.path.append(os.path.dirname(theme_path))
    import baseTheme
    baseTheme.apply(c)

#fonts
c.fonts.completion.entry = "11pt JetBrainsMono Nerd Font"
c.fonts.statusbar = "11pt JetBrainsMono Nerd Font"
c.fonts.downloads = "11pt JetBrainsMono Nerd Font"
c.fonts.prompts = "11pt JetBrainsMono Nerd Font"
c.fonts.tabs.selected = "14pt JetBrainsMono Nerd Font"
c.fonts.tabs.unselected = "14t JetBrainsMono Nerd Font"

# Appearance
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"
c.tabs.show = "never"
c.statusbar.show = "never"

# Start page
c.url.start_pages = ["https://www.google.com"]

# Downloads folder
c.downloads.location.directory = "~/Downloads"

# speed:
c.content.images = True
c.qt.args = ["disable-gpu", "disable-software-rasterizer"]
c.qt.args += ["--use-gl=swiftshader"]
c.completion.shrink = True
c.tabs.indicator.width = 0

#shortcuts
c.url.searchengines = {
    'DEFAULT':  'https://google.com/search?hl=en&q={}',
}

