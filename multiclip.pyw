#! python3

# multiclip.pyw - A program which save content from clipboard to shelve file under some "keyword" and when needed
# copy to the clipboard list of all keywords or content saved under keyword.

# Usage: py.exe multiclip.pyw save <keyword> - Save clipboard content to shelve file under some <keyword>
#        py.exe multiclip.pyw list - Copy to clipboard list of all keywords from shelve file.
#        py.exe multiclip.pyw <keyword> - Copy to clipboard content of <keyword>

# TODO: Import essential modules.
import sys
import pyperclip
import shelve

# TODO: Open shelve module.
mc_shelf = shelve.open('multiclip')

# TODO: Save content to shelve.
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    mc_shelf[sys.argv[2]] = pyperclip.paste()
    print('Content saved to shelve file under "{}" keyword.'.format(sys.argv[2]))

# TODO: Copy to clipboard list of all keywords.


# TODO: Copy to clipboard content of keyword.
# TODO: Delete keyword content.
# TODO: Open new clean file.
