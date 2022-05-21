

print("***********************************************************")
# Writing to an existing file.
my_file = open("exex1.txt", 'w')
l1 = "This is line 1.\n"
l2 = "This is line 2.\n"
l3 = "This is line 3.\n"
my_file.write(l1 + l2 + l3)
my_file.close()
print("***********************************************************")
# Reading from an existing file.
my_file = open("exex1.txt", 'r')
fileContent = my_file.read()
print(fileContent)
my_file.seek(0)
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())
my_file.close()

print("***********************************************************")
# Iterate through each line of a file using a loop.
my_file = open("exex1.txt")
print(my_file.mode)  # r

# Iterate through each line using a loop

with open("exex1.txt", "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i += 1

print("***********************************************************")
# Read all lines and save as a list
with open("exex1.txt") as file1:
    file_list = file1.readlines()

print(type(f"type(file1): {type(file1)}"))
print(type(f"type(file_list): {type(file_list)}"))
print(f"file_list[0]: {file_list[0]}")  # print the first line
print(f"file_list[1]: {file_list[1]}")  # print the second line
print(f"file_list[2]: {file_list[2]}")  # print the third line
print(f"file_list: {file_list}")  # print the whole list
print("***********************************************************")
# Opening a file in write mode with the same name as of a file that already exists, will replace the current file.

lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open("exex1.txt", "w") as file1:
    for line in lines:
        file1.write(line)

with open("exex1.txt") as file1:
    file_list = file1.readlines()

print(file_list[0])
print(file_list[2])
print(file_list)
print("***********************************************************")
# We can also append to an existing file which won't replace the current file or its contents.
with open("exex1.txt", 'a') as file1:
    file1.write("This is line D.\n")

with open("exex1.txt") as file1:
    file_list = file1.readlines()

print(file_list)
print("***********************************************************")
# Copy the contents of one file to another file, new file in this case.
with open("exex1.txt", 'r') as readfile:
    with open("exex2.txt", 'w') as writefile:
        for line in readfile:
            writefile.write(line)

with open("exex2.txt") as file1:
    print(f"file1.readlines():\n {file1.readlines()}")

print("***********************************************************")
"""
    Additional modes:
    r+ is used for reading and writing. Can not truncate the file.
    w+ is used for writing and reading. Truncates the file i.e. overwrites and deletes all pre-existing data.
    a+ is used for appending and reading. Creates a new file, if none exists.
    
    To work with a file on existing data, use r+ and a+. 
"""

# Let's open a file in reading and writing mode with r+
with open("exex2.txt", 'a+') as file1:
    file1.write("This is line E\n")
    print(file1.read())  # This will print nothing because of our location in the file.

print("***********************************************************")
# opening the file with mode 'w' moves the cursor to beginning of the file and deletes everything.
# Opening the file is append mode 'a' moves the cursor to the very end of the file and then add new text.
# .tell() returns the current position in bytes.
# .seek(offset, from) changes the position by 'offset' bytes with respect to 'from'.
# From can take the value of 0, 1, 2 corresponding to beginning, relative to current position and end.

with open("exex2.txt", 'a+') as file1:  # a+ is used for appending and reading. Creates a new file, if none exists.
    print("Initial Location: {}".format(file1.tell()))

    data = file1.read()
    if not data:  # empty strings return False in Python.
        print("Read nothing")
    else:
        print(data)

    print("Location after read: {}".format(file1.tell()))
    file1.seek(0, 0)  # Move 0 bytes from beginning.

    print("\nNew Location : {}".format(file1.tell()))
    data = file1.read()
    if not data:
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(file1.tell()))

print("***********************************************************")
# r+ is used for reading and writing. Can not truncate the file.
# While using r+ mode, it could be useful to .truncate() method at the end of data to reduce the file to data and
# delete everything that follows.

with open("exex2.txt", 'r+') as file1:
    data = file1.readlines()

    file1.seek(0, 0)  # Go to the beginning of the file
    file1.write("Line 1" + "\n")
    file1.write("Line 2" + "\n")
    file1.write("Line 3" + "\n")

    # First run this file without uncommenting the line below. Then run it after uncommenting the line below.
    # file1.truncate()
    file1.seek(0, 0)
    print(file1.read())
print("***********************************************************")
