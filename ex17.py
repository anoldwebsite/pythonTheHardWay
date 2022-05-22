from sys import argv
from os.path import exists

script, from_file, to_file = argv

    
print(f"Copying from {from_file} to {to_file}.")

# The two lines below could be written as one like this: in_data = open(from_file).read()
in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")

in_file.close()
out_file.close()


# open(to_file, 'w').write(open(from_file).read())

"""
    with open(from_file) as f:
    with open(to_file, 'w') as t:
        t.write(f.read())
"""


"""
>>> with open("exex1.txt", 'r') as read_file:
...     with open("temporary3.txt", 'w') as write_file:
...             write_file.write(read_file.read())
... 
61
>>> with open("temporary3.txt") as file1:
...     print(file1.read())
... 
This is line A
This is line B
This is line C
This is line D.

>>> with open("temporary3.txt") as file1:
...     line = file1.readline()
...     print(line)
... 
This is line A

>>> with open("temporary3.txt") as file2:
...     lines = file2.readlines()
...     print(lines)
... 
['This is line A\n', 'This is line B\n', 'This is line C\n', 'This is line D.\n']
>>> with open("temporary3.txt") as file3:
...     lines = file3.readlines()
...     for line in lines:
...             print(line)
... 
This is line A

This is line B

This is line C

This is line D.

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> read_file = "exex1.txt"
>>> write_file = "temporary3.txt"
>>> with open(read_file):
...     
... 
  File "<stdin>", line 3
    
    ^
IndentationError: expected an indented block
>>> with open(read_file) as file1:
...     first_line = file1.readline()
...     print(first_line)
...     second_line = file1.readline()
...     print(second_line)
... 
This is line A

This is line B

>>> text = ''
>>> with open(read_file) as file1:
...     text += file1.readline()
...     text += file1.readline()
... 
>>> print(text)
This is line A
This is line B

>>> with open(read_file) as file1:
...     lines = file1.readlines()
...     print(lines)
... 
['This is line A\n', 'This is line B\n', 'This is line C\n', 'This is line D.\n']
>>> with open(read_file) as file1:
...     lines = file1.readlines()
...     for line in lines:
...             print(line)
... 
This is line A

This is line B

This is line C

This is line D.

>>> some_list = []
>>> with open(read_file) as file1:
...     lines = file1.readlines()
...     for line in lines:
...             some_list.append(line)
... 
>>> len(some_list)
4
>>> print(some_list)
['This is line A\n', 'This is line B\n', 'This is line C\n', 'This is line D.\n']
>>> for line in some_list:
...     print(line)
... 
This is line A

This is line B

This is line C

This is line D.

>>>
"""


