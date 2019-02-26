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
# TODO: Save content to shelve file under keyword.

# TODO: Delete keyword from shelve file.

# TODO: Delete all keyword, start with new shelve file.

# TODO: Copy all saved keywords to the clipboard.

# TODO: Copy keyword content to the clipboard. 
