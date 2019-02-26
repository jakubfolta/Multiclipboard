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
