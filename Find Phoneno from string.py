#! python3
#Finding phone number using string operations

def isPhoneNumber(no):
    if len(no)!=12:
        return False
    for i in range(0,3):
        if not no[i].isdecimal():
            return False
    if no[3]!='-':
        return False
    for i in range(4,7):
        if not no[i].isdecimal():
            return False
    if no[7]!='-':
        return False
    for i in range(8,12):
        if not no[i].isdecimal():
            return False
    return True


msg='My phone no is 417-999-4244 for personal use'

for i in range(len(msg)):
    no=msg[i:i+12]
    if isPhoneNumber(no):
        print('Phone no is found',no)