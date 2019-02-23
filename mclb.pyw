#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mclb.pyw save <keyword> - Save content from clipboard to shelf file under keyword name.
#        py.exe mclb.pyw list - Copy saved keywords to the clipboard.
#        py.exe mclb.pyw <keyword> - Copy content for this keyword to the clipboard.

import pyperclip
import sys
import shelve

mcb_shelf = shelve.open('mclb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print('Content saved under "{}" keyword.'.format(sys.argv[2]))
# Saves clipboard content to shelve.
elif len(sys.argv) == 2:
# TODO: Load keyword content to clipboard.
    if sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print('Content for "{}" keyword copied to clipboard'.format(sys.argv[1]))
    

# TODO: Copy all keywords to clipboard.


mcb_shelf.close()
