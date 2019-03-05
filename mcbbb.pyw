#! python3

# mcbbb.pyw - Saves clipboard content to shelve file and
# load it later for quick pastingself.

# Usage: py.exe mcbbb.pyw save <keyword> - save content to shelve file under <keyword>
#        py.exe mcbbb.pyw <keyword> - copy to clipboard content saved under <keyword>
#        py.exe mcbbb.pyw list - copy to the clipboard all keywords saved to the shelve file

import sys
import shelve
import pyperclip
# Open shelve file
mc_shelf = shelve.open('mcbbb')
# TODO: Save copied content under keyword to shelve file
# TODO: Load keyword content back to the clipboard
# TODO: Load to the clipboard all keywords from shelve file
