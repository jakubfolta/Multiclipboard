#! python3

# Usage : py.exe emcb.pyw save <keyword>
#         py.exe emcb.pyw delete <keyword>
#         py.exe emcb.pyw deleteall
#         py.exe emcb.pyw list
#         py.exe emcb.pyw <keyword>

import sys
import pyperclip
import shelve

# Open shelve file.
emcb_shelf = shelve.open('emcb')

# Save content to shelve file under keyword.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    emcb_shelf[sys.argv[2]] = pyperclip.paste()
    print('Clipboard content saved under "{}".'.format(sys.argv[2]))
    
# Delete keyword from shelve file.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    del emcb_shelf[sys.argv[2]]
    print('"{}" keyword deleted.'.format(sys.argv[2]))
    
# Delete all keyword, start with new shelve file.
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delall':
    emcb_shelf = shelve.open('emcb', flag = 'n')
    print('All content deleted. New file opened.')
    
# Copy all saved keywords to the clipboard.
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(emcb_shelf.keys())))
    print('Keywords copied to clipboard: {}'.format(list(emcb_shelf.keys())))
    
# Copy keyword content to the clipboard.
elif len(sys.argv) == 2 and sys.argv[1] in emcb_shelf:
    pyperclip.copy(emcb_shelf[sys.argv[1]])
    print('"{}" keyword content saved to clipboard.'.format(sys.argv[1]))
emcb_shelf.close()


