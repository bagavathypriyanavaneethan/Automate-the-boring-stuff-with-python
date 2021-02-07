# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:51:02 2021

@author: Bagavathi Priya
"""

import os
>>> os.getcwd()
'C:\\Users\\Bagavathi Priya'

>>> os.path.abspath('.\BOOK')
'C:\\Users\\Bagavathi Priya\\BOOK'

>>> os.path.abspath('.\\BOOK')
'C:\\Users\\Bagavathi Priya\\BOOK'

>>> os.path.abspath('.')
'C:\\Users\\Bagavathi Priya'

>>> os.getcwd()
'C:\\Users\\Bagavathi Priya'

>>> os.path.isfile('BOOK')
False

>>> os.path.isdir('BOOK')
False

>>> os.path.exists('D;\\')
False

>>> os.path.exists('D:\\')
True

#shelve module to save variables 
>>> os.getcwd()
'C:\\Users\\Bagavathi Priya'

>>> import shelve
>>> shelfFile=shelve.open('mydata')
>>> cats=['Bibi','Anzz','abi']
>>> shelfFile['cats']=cats
>>> shelfFile.close()


>>> shelfFile=shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Bibi', 'Anzz', 'abi']
>>> shelfFile.close()


>>> shelfFile=shelve.open('mydat')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> list(shelfFile.keys())
[]
>>> shelfFile=shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Bibi', 'Anzz', 'abi']]
>>> shelfFile.close()


#Using pprint to save in text files 
>>> import pprint
>>> cats=[{'name':'bibi','type':'chubby'},{'name':'anzz','type':'angry'}]
>>> cats
[{'name': 'bibi', 'type': 'chubby'}, {'name': 'anzz', 'type': 'angry'}]
>>> pprint.pformat(cats)
"[{'name': 'bibi', 'type': 'chubby'}, {'name': 'anzz', 'type': 'angry'}]"

>>> fileObj=open('mypet.py','w')
>>> fileObj.write('cats = '+pprint.pformat(cats)+'\n')
79
>>> fileObj.close()

#We can also import like python modules
>>> import mypet
>>> mypet.cats
[{'name': 'bibi', 'type': 'chubby'}, {'name': 'anzz', 'type': 'angry'}]
>>> mypet.cats[0]
{'name': 'bibi', 'type': 'chubby'}
>>> mypet.cats[0]['type']
'chubby'
