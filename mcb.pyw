#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keywords to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')
# Add "flag = n" as a second argument when opening to clear shelf files.
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print('Content saved to file with "{}" keyword.'.format(sys.argv[2]))
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print('Content for "{}" keyword copied to your clipboard. Just paste it!'.format(sys.argv[1]))
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print('Keywords saved: {}'.format(list(mcb_shelf.keys())))

        

mcb_shelf.close()



