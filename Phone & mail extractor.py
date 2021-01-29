#! python3
#Phone and email address extractor 

import pyperclip,re

#Regular expression for phone number 
phoneRegex=re.compile(r'''(
    (\d{3}|(\d{3}\))?       #areacode
    (\s|-|\.)?              #separator 
    (\d{3})                 #three digit 
    (\s|-|\.)               #separator 
    (\d{4})                 #four digit 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
    )''',re.VERBOSE)

#Regular expression for email address
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+      #username
    @                      #@symbol
    [a-zA-Z0-9.-]+        #domain name
    (\.[a-zA-Z]{2,4})     #eg:.co
    )''',re.VERBOSE)

#Find match in clipboard text 
text=str(pyperclip.paste())

matches=[]

#To find all the phone number
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    
    if groups[8] != '':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)

#To find all the email address
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
#Copy results to clipboards
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No phone or email address is found")
