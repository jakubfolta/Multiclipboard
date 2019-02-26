#! python3

# Usage : py.exe emcb.pyw save <keyword>
#         py.exe emcb.pyw delete <keyword>
#         py.exe emcb.pyw deleteall
#         py.exe emcb.pyw list
#         py.exe emcb.pyw <keyword>

import sys
import pyperclip
import shelve

# TODO: Open shelve file.
emcb_shelf = shelve.open('emcb')
# Save content to shelve file under keyword.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    emcb_shelf[sys.argv[2]] = pyperclip.paste()
    print('Clipboard content saved under "{}".'.format(sys.argv[2]))
# Delete keyword from shelve file.
elif len(sys.argv) == 3 and sys.argv[1] == 'del':
    del emcb_shelf[sys.argv[2]]
    print('"{}" keyword deleted.'.format(sys.argv[2]))
# TODO: Delete all keyword, start with new shelve file.
elif len(sys.argv) == 2 and sys.argv[1] == 'delall':
    emcb_shelf = shelve.open('emcb', flag = 'n')
    print('All content deleted. New file opened.')
# TODO: Copy all saved keywords to the clipboard.

# TODO: Copy keyword content to the clipboard. 
