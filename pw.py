#! python3
# pw.py - An insecure password locker

password={'email':'bagavathypriya5936@gmail.com',
          'blog':'medium',
          'luggage':'12345'}

import sys,pyperclip

if len(sys.argv)<2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()
    
account=sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('Password for '+account+' is copied to clipboard')

else:
    print('There is no account named '+account)
    
'''
Bat file to be store in C:\Windows as pw.bat
@py.exe D:\Education\python\Automate_bore_stuff_wd_python\pw.py %*
@pause
'''

'''
To run press Win+R then give the command as
pw <account>
eg: pw blog
o/p: medium
'''
