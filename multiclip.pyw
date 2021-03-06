#! python3

# multiclip.pyw - A program which save content from clipboard to shelve file under some "keyword" and when needed
# copy to the clipboard list of all keywords or content saved under keyword.

# Usage: py.exe multiclip.pyw save <keyword> - Save clipboard content to shelve file under some <keyword>
#        py.exe multiclip.pyw list - Copy to clipboard list of all keywords from shelve file.
#        py.exe multiclip.pyw <keyword> - Copy to clipboard content of <keyword>
#        py.exe multiclip.pyw del <keyword> - Delete <keyword> and its content from shelve file.
#        py.exe multiclip.pyw delall - Open new empty shelve file ready to read and write.

# Import essential modules.
import sys
import pyperclip
import shelve

# Open shelve module.
mc_shelf = shelve.open('multiclip')

# Save content to shelve.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mc_shelf[sys.argv[2]] = pyperclip.paste()
        print('Content saved to shelve file under "{}" keyword.'.format(sys.argv[2]))

# Delete keyword & its content from shelve file.
    elif sys.argv[1].lower() == 'del' and sys.argv[2] in mc_shelf:
        del mc_shelf[sys.argv[2]]
        print('"{}" keyword and its content deleted from shelve file.'.format(sys.argv[2]))

# Copy to clipboard list of all keywords.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mc_shelf.keys())))
        print('Keywords: {} \ncopied to clipboard.'.format(list(mc_shelf.keys())))

# Copy to clipboard content of keyword.
    elif sys.argv[1] in mc_shelf:
        pyperclip.copy(mc_shelf[sys.argv[1]])
        print('"{}" content copied to clipboard.'.format(sys.argv[1]))

# Open new clean file.
    elif sys.argv[1].lower() == 'delall':
        mc_shelf = shelve.open('multiclip', flag = 'n')
        print('New shelve file created.')
