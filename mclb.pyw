#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mclb.pyw save <keyword> - Save content from clipboard to shelf file under keyword name.
#        py.exe mclb.pyw list - Copy saved keywords to the clipboard.
#        py.exe mclb.pyw <keyword> - Copy content for this keyword to the clipboard.

import pyperclip
import sys
import shelve

mcb_shelf = shelve.open('mclb') # Clear file - "flag = n" as 2nd argument.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print('Content saved under "{}" keyword.'.format(sys.argv[2]))
# Saves clipboard content to shelve.
elif len(sys.argv) == 2:
# Load keyword content to clipboard.
    if sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print('Content for "{}" keyword copied to clipboard'.format(sys.argv[1]))
# Copy all keywords to clipboard.
    elif sys.argv[1] == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print('Keywords saved: {}'.format(list(mcb_shelf.keys())))
mcb_shelf.close()
