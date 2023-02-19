Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Toey'
print(name)
Toey
type(name)
<class 'str'>
name.lower()
'toey'
name.upper()
'TOEY'
name.count
<built-in method count of str object at 0x000001F23A919BF0>
name.format
<built-in method format of str object at 0x000001F23A919BF0>
friend = 'Jimin'
print('Hi! Jimin How r u?')
Hi! Jimin How r u?
print('Hi!' +friend + 'How r u?')
Hi!JiminHow r u?
print('Hi! ' +friend + ' How r u?')
Hi! Jimin How r u?
money = 10
print('Jimin give me 10 baht')
Jimin give me 10 baht
print(friend + ' give me ' + money + 'baht')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(friend + ' give me ' + money + 'baht')
TypeError: can only concatenate str (not "int") to str

type(money)
<class 'int'>
print(friend + ' give me ' str(money) + 'baht')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(friend + ' give me' + str(money) + ' baht.')
Jimin give me10 baht.
print('{} give me {} baht'.format(friend,money))
Jimin give me 10 baht
print(f'{friend} give me {money} baht')
Jimin give me 10 baht
money = 1820903232423232323
print(f'{money:,}')
1,820,903,232,423,232,323
print(f'{money:,.2f}')
1,820,903,232,423,232,256.00
1,820,903,232,423,232,256.00
(1, 820, 903, 232, 423, 232, 256.0)
print('{:,.2f}' .format(money))
1,820,903,232,423,232,256.00


import math
math
math.pi
3.141592653589793
math.pi * (5 ** 2)
78.53981633974483
from datetime import datetime
datetime.now()
datetime.datetime(2023, 2, 11, 22, 53, 52, 713435)
datetime.now().strtime('%Y%m%d %H:%M:%S')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    datetime.now().strtime('%Y%m%d %H:%M:%S')
AttributeError: 'datetime.datetime' object has no attribute 'strtime'. Did you mean: 'strftime'?
Traceback (most recent call last):
    datetime.now().strftime('%Y%m%d %H:%M:%S')
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
datetime.now().strftime('%y%m%d %H:%M%S')
'230211 22:5551'
datetime.now().strftime('%y.%m.%d %H:%M%S')
'23.02.11 22:5613'
datetime.now().strftime('%y.%m.%d %H:%M:%S')
'23.02.11 22:56:23'
import random
random.radint(1,7)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    random.radint(1,7)
AttributeError: module 'random' has no attribute 'radint'. Did you mean: 'randint'?
random.randint(1,7)
7
store = ['7-11','Fammart','Lawson']
random.choice(store)
'Lawson'

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python101/GUI-knowledge.py", line 12, in <module>
    B2 = Buttom(GUI, text='How much we have?')
NameError: name 'Buttom' is not defined. Did you mean: 'Button'?

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python101/GUI-knowledge.py", line 12, in <module>
    B2 = Buttom(GUI, text='How much we have?')
NameError: name 'Buttom' is not defined. Did you mean: 'Button'?

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python101/GUI-knowledge.py", line 12, in <module>
    B2 = Buttom(GUI, text='How much we have?')
NameError: name 'Buttom' is not defined. Did you mean: 'Button'?

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python101/GUI-knowledge.py", line 12, in <module>
    B2 = Buttom(GUI,text='How much we have?')
NameError: name 'Buttom' is not defined. Did you mean: 'Button'?

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python101/GUI-knowledge.py", line 19, in <module>
    FB1 = Frame(GUI,text='money') #board
  File "C:\Python311\Lib\tkinter\__init__.py", line 3190, in __init__
    Widget.__init__(self, master, 'frame', cnf, {}, extra)
  File "C:\Python311\Lib\tkinter\__init__.py", line 2628, in __init__
    self.tk.call(
_tkinter.TclError: unknown option "-text"

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
>>> 
= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
>>> 
= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py

= RESTART: C:/Users/user/Documents/Python101/GUI-knowledge.py
