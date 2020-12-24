#! python3
#bulletPointAdder.py Adding bullet points to the start of line

import pyperclip
text=pyperclip.paste()

#TODO separate lines and add stars

#Separate lines by \n and add stars *

lines=text.split('\\n') 
print('no of lines',len(lines))
for i in range(len(lines)):
    lines[i]="* "+lines[i]


#Pyperclip expecting the string , so converting again to string from list type.

text= '\n'.join(lines)
pyperclip.copy(text)
print('The text is copied to clipboard')

'''* List of bags\nList of purses
* List of bags\nList of purses'''

'''
o/p
* List of bags
* List of purses
'''