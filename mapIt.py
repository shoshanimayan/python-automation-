# launches a map in browser using an address from the command line

import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    address =' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
    
