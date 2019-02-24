#! python3

# Multiclipboard for saving content to shelve file and
# loading it later for quick pasting.

# Usage: py.exe mcbb.pyw save <keyword> - save content to shelve file under entered keyword.
#        py.exe mcbb.pyw list - copy list of all keywords to clipboard.
#        py.exe mcbb.pyw <keyword> - copy content saved under keyword to clipboard.

import sys
import shelve
import pyperclip

mcbb_shelf = shelve.open(mcbb)
# Save content under keyword.
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    mcbb_shelf[sys.argv[2]] = pyperclip.paste()
    print('Content from clipboard saved to the shelve file under "{}" keyword.'.format(sys.argv[2]))

# TODO: Copy all keywords to clipboard.

# TODO: Copy keyword content to clipboard. 
