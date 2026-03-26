Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> x = 5
>>> _x=5
>>> &&^%x=12
SyntaxError: invalid syntax
>>> x y=12
SyntaxError: invalid syntax
>>> xy=12
>>> 
>>> x = 12
>>> type(x)
<class 'int'>
>>> 
>>> x = 12.435
>>> type(x)
<class 'float'>
>>> 
>>> x = "hey"
>>> type(x)
<class 'str'>
>>> 
>>> x = 2+5j
>>> type(x)
<class 'complex'>
>>> x.real
2.0
>>> x.imag
5.0
>>> x = None
x
x
x
x

x = 3
x
3
x
3
#String
#String is immutable data type
#immutable - which cannot be changed...
x = "hey welcome TO PYTHON"
len(x)
21
x = "uday"
len(x)
4
x = "hey welcome TO PYTHON"
x.upper()
'HEY WELCOME TO PYTHON'
x.lower()
'hey welcome to python'
x.title()
'Hey Welcome To Python'
x.capitalize()
'Hey welcome to python'
x
'hey welcome TO PYTHON'
y = "uday"
y[0]
'u'
y[-1]
'y'
x[-1]
'N'
x
'hey welcome TO PYTHON'
x.swapcase()
'HEY WELCOME to python'
x
'hey welcome TO PYTHON'
x.find("e")
1
x.rfind("e")
10
x.find("e",2)
5
x.index("e",2)
5
x.find("X")
-1
x.index("X")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x.index("X")
ValueError: substring not found
