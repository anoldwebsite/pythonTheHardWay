# reading a file from computer disk
from sys import argv  # sys is a package
script, filename = argv

txt = open(filename)  # returns a file object

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()  # “It’s important to close files when you are done with them.”

print("Type the filename again please:")
file_again = input(">")
txt_again = open(file_again)
contents = txt_again.read()
txt_again.close()
print(contents)

"""
    Study drills:
    * Start python3.9 to start the python3.9 shell, and use open from the prompt 
    just like in the program in ex15.py. Notice how you can open files and run 
    read on them from within python3.9.
    
    *****************************************************
    
anoldwebsite$ python3.9

Python 3.9.12 (v3.9.12:b28265d7e6, Mar 23 2022, 18:17:11) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open('ex1.py', 'r')
>>> print(f.read())
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('"I said" do not touch this.')
print("Printing yet another line.")
# This is a comment that is not executed when the program runs.
# This symbol is called octothorpe or a pound sign or hash sign or mesh.

>>> f.close()
>>> print(f.read())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> 

    *****************************************************
>>> f = open('ex1.py', 'r')
>>> oneline = f.readline()
>>> print(oneline)
print("Hello World!")
>>> f.close()
    *****************************************************
    # Creating a file on python shell
    >>> open('exex1.txt', 'x')
<_io.TextIOWrapper name='exex1.txt' mode='x' encoding='UTF-8'>
    *****************************************************
    # Open the file in writing mode.
    >>> open('exex1.txt', 'w')
<_io.TextIOWrapper name='exex1.txt' mode='w' encoding='UTF-8'>
    *****************************************************
    # Writing to a file.
    >>> myfile = open("exex1.txt", 'w')
>>> line1 = "This is line 1 in file exex1.txt\n"
>>> line2 = "This is line2 which is being written into this file from Python shell.\n"
>>> line3 = "Line 3: These lines will be written to the file from Python shell using command function write()\n"
>>> myfile.write(line1 + line2 + line3)
201
>>> myfile.close()
    *****************************************************
    # Open file in write mode and write text to it and then close the file, open it again and read text from it.
>>> myfile = open("exex1.txt", "w")
>>> myfile = open("exex1.txt", 'w')
>>> myfile.writelines(["This is line1.", "This is line2.", "This is line3."])
>>> myfile.close()
>>> myfile = open("exex1.txt", 'r')
>>> fileContent = myfile.read()
>>> print(fileContent)

This is line1.This is line2.This is line3.
>>> 
>>> print(myfile.read())

>>> myfile.readlines()
[]
>>> myfile.readline()
''
>>> myfile.close()
>>> myfile = open("exex1.txt","r")
>>> print(myfile.read())
>>> This is line1.This is line2.This is line3.
   *****************************************************
   # Text inside the file before this exercise is like this:
   This is line1.
   This is line2.
   This is line3.
   
>>> with open("exex1.txt", "r") as file1:
...     i = 0
...     for line in file1:
...             print("Iteration", str(i), ": ", line)
...             i += 1
... 
Iteration 0 :  This is line1.

Iteration 1 :  This is line2.

Iteration 2 :  This is line3.
>>>
   *****************************************************
    # open file in both read and write mode
    >>> open("exex1.txt", 'r+')
<_io.TextIOWrapper name='exex1.txt' mode='r+' encoding='UTF-8'>
>>> myfile = open("exex1.txt", 'r+')
>>> myfile.readlines()
>>> ['This is line1.This is line2.This is line3.']
>>> myfile.readline()
''
myfile.write("This file was opened in both read and write mode and now I'm writing this line to it.") 
85
>>> myfile.readlines()
[]
>>> myfile.readline()
''

    *****************************************************
    # split lines into words in a text file and then making a set to find unique words 
    >>> myfile = open("exex1.txt","r")
>>> data = myfile.readlines()
>>> type(data)
<class 'list'>
>>> for line in data:
...     words = line.split()
...     print(words)
... 
['I', 'can', 'write', 'multiple', 'lines', 'to', 'a', 'file', 'using', 'function', 'writelines()', 'and', 'passing', 'the', 'text', 'to', 'this', 'function', 'as', 'string.We', 'can', 'also', 'write', 'multiple', 'lines', 'to', 'a', 'file', 'using', 'special', 'characters', 'e.g.', 'back', 'slash', 'n', 'for', 'new', 'line.This', 'file', 'was', 'opened', 'in', 'both', 'read', 'and', 'write', 'mode', 'and', 'now', "I'm", 'writing', 'this', 'line', 'to', 'it.']

>>> words=[]
>>> for line in data:
...     words.append(line.split())
... 
>>> type(words)
<class 'list'>
>>> len(words)
1
>>> print(words[0])
['I', 'can', 'write', 'multiple', 'lines', 'to', 'a', 'file', 'using', 'function', 'writelines()', 'and', 'passing', 'the', 'text', 'to', 'this', 'function', 'as', 'string.We', 'can', 'also', 'write', 'multiple', 'lines', 'to', 'a', 'file', 'using', 'special', 'characters', 'e.g.', 'back', 'slash', 'n', 'for', 'new', 'line.This', 'file', 'was', 'opened', 'in', 'both', 'read', 'and', 'write', 'mode', 'and', 'now', "I'm", 'writing', 'this', 'line', 'to', 'it.']
>>> print(words)
[['I', 'can', 'write', 'multiple', 'lines', 'to', 'a', 'file', 'using', 'function', 'writelines()', 'and', 'passing', 'the', 'text', 'to', 'this', 'function', 'as', 'string.We', 'can', 'also', 'write', 'multiple', 'lines', 'to', 'a', 'file', 'using', 'special', 'characters', 'e.g.', 'back', 'slash', 'n', 'for', 'new', 'line.This', 'file', 'was', 'opened', 'in', 'both', 'read', 'and', 'write', 'mode', 'and', 'now', "I'm", 'writing', 'this', 'line', 'to', 'it.']]

>>> a_set = set(words[0])
>>> type(a_set)
<class 'set'>
>>> len(a_set)
39
>>> for s in a_set:
...     print(s)
... 
multiple
slash
opened
this
it.
function
I'm
mode
line
special
both
new
was
writelines()
write
can
string.We
I
as
and
a
to
read
back
writing
file
text
now
also
the
characters
n
in
using
lines
passing
e.g.
for
line.This
>>> len(a_set)
39
>>> len(words[0])
55
>>>
   
>>> type(a_set)
<class 'set'>
>>> len(a_set)
39
>>> a_dic = {unique:words[0].count(unique) for unique in a_set} 
>>> type(a_dic)
<class 'dict'>
>>> len(a_dic)
39
>>> for key in a_dic:
...     print(key, '->', a_dic[key])
... 
multiple -> 2
slash -> 1
opened -> 1
this -> 2
it. -> 1
function -> 2
I'm -> 1
mode -> 1
line -> 1
special -> 1
both -> 1
new -> 1
was -> 1
writelines() -> 1
write -> 3
can -> 2
string.We -> 1
I -> 1
as -> 1
and -> 3
a -> 2
to -> 4
read -> 1
back -> 1
writing -> 1
file -> 3
text -> 1
now -> 1
also -> 1
the -> 1
characters -> 1
n -> 1
in -> 1
using -> 2
lines -> 2
passing -> 1
e.g. -> 1
for -> 1
line.This -> 1
>>> 
>>> print("We can  use funciton .item() to return a new view of our dictionary a_dic")
We can  use funciton .item() to return a new view of our dictionary a_dic
>>> a_view = a_dic.items()
>>> type(a_view)
<class 'dict_items'>
>>> len(a_view)
39
>>> a_view
dict_items([('multiple', 2), ('slash', 1), ('opened', 1), ('this', 2), ('it.', 1), ('function', 2), ("I'm", 1), ('mode', 1), ('line', 1), ('special', 1), ('both', 1), ('new', 1), ('was', 1), ('writelines()', 1), ('write', 3), ('can', 2), ('string.We', 1), ('I', 1), ('as', 1), ('and', 3), ('a', 2), ('to', 4), ('read', 1), ('back', 1), ('writing', 1), ('file', 3), ('text', 1), ('now', 1), ('also', 1), ('the', 1), ('characters', 1), ('n', 1), ('in', 1), ('using', 2), ('lines', 2), ('passing', 1), ('e.g.', 1), ('for', 1), ('line.This', 1)])
>>>
>>> print("Give me just the keys from the dictionary a_dic")
Give me just the keys from the dictionary a_dic
>>> a_dic.keys()
dict_keys(['multiple', 'slash', 'opened', 'this', 'it.', 'function', "I'm", 'mode', 'line', 'special', 'both', 'new', 'was', 'writelines()', 'write', 'can', 'string.We', 'I', 'as', 'and', 'a', 'to', 'read', 'back', 'writing', 'file', 'text', 'now', 'also', 'the', 'characters', 'n', 'in', 'using', 'lines', 'passing', 'e.g.', 'for', 'line.This'])
>>> print("Give me only the values from the dictionary a_dict") 
Give me only the values from the dictionary a_dict
>>> a_dic.values()
dict_values([2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 3, 2, 4, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1])

>>> for value in a_dic.values():
...     print(value)
... 
2
1
1
2
1
2
1
1
1
1
1
1
1
1
3
2
1
1
1
3
2
4
1
1
1
3
1
1
1
1
1
1
1
2
2
1
1
1
1
>>>
>>> for key in a_dic.keys():
...     print(key)
... 
multiple
slash
opened
this
it.
function
I'm
mode
line
special
both
new
was
writelines()
write
can
string.We
I
as
and
a
to
read
back
writing
file
text
now
also
the
characters
n
in
using
lines
passing
e.g.
for
line.This
>>>
>>> highest_frequency = 0
>>> highest_frequency
0
>>> a_dic
{'multiple': 2, 'slash': 1, 'opened': 1, 'this': 2, 'it.': 1, 'function': 2, "I'm": 1, 'mode': 1, 'line': 1, 'special': 1, 'both': 1, 'new': 1, 'was': 1, 'writelines()': 1, 'write': 3, 'can': 2, 'string.We': 1, 'I': 1, 'as': 1, 'and': 3, 'a': 2, 'to': 4, 'read': 1, 'back': 1, 'writing': 1, 'file': 3, 'text': 1, 'now': 1, 'also': 1, 'the': 1, 'characters': 1, 'n': 1, 'in': 1, 'using': 2, 'lines': 2, 'passing': 1, 'e.g.': 1, 'for': 1, 'line.This': 1}
>>>
>>> for key in a_dic:
...     if a_dic[key] >= highest_frequency:
...             highest_frequency = a_dic[key]
... 
>>> def get_value_from_key(v, some_dic):
...     for key, value in some_dic.items():
...             if v == value:
...                     return key
...     return "Key does not exits."
... 
>>> key = get_value_from_key(highest_frequency, a_dic)
>>> print(f"Frequency of word '{key}' is: {highest_frequency}.")
Frequency of word 'to' is: 4.
    ********************************************
    " open a file, read all contents and then use function seek(0) to go to the beginning of the file again.
>>> myfile.close()
>>> file = open("exex1.txt", 'r+')
>>> file.read()
"I can write multiple lines to a file using function writelines() and passing the text to this function as string.We can also write multiple lines to a file using special characters e.g. back slash n for new line.This file was opened in both read and write mode and now I'm writing this line to it."
>>> file.read()
''
>>> file.seek(0)
0
>>> file.read()
"I can write multiple lines to a file using function writelines() and passing the text to this function as string.We can also write multiple lines to a file using special characters e.g. back slash n for new line.This file was opened in both read and write mode and now I'm writing this line to it."
>>> file.read()
''
>>> file.seek(0)
0
>>> file.read()
"I can write multiple lines to a file using function writelines() and passing the text to this function as string.We can also write multiple lines to a file using special characters e.g. back slash n for new line.This file was opened in both read and write mode and now I'm writing this line to it."
>>>

 *****************************************************
 # truncate() function a file empties a file.
>>> myfile = open("exex1.txt", 'r+')
>>> myfile.read()
"I can write multiple lines to a file using function writelines() and passing the text to this function as string.We can also write multiple lines to a file using special characters e.g. back slash n for new line.This file was opened in both read and write mode and now I'm writing this line to it."
>>> myfile.read()
''
>>> myfile.truncate()
297
>>> myfile.read()
''
>>> myfile.seek(0)
0
>>> myfile.read()
"I can write multiple lines to a file using function writelines() and passing the text to this function as string.We can also write multiple lines to a file using special characters e.g. back slash n for new line.This file was opened in both read and write mode and now I'm writing this line to it."
>>> myfile.read()
''
>>> myfile.seek(0)
0
>>> myfile.truncate()
0
>>> myfile.seek(0)
0
>>> myfile.read()
''
>>> myfile.close()
"""

