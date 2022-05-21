"""
    Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills. <br>
Given the file `currentMem`, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the `exMem` file. Make sure that the format of the original files in preserved.   (*Hint: Do this by reading/writing whole lines and ensuring the header remains* ) <br>
Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the `cleanFiles` function.

"""


"""
    # Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee = ('yes', 'no')


def genFiles(current, old):
    with open(current, 'w+') as writefile:  # w+ is used for writing and reding. Truncates the file
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


genFiles(memReg, exReg)
"""

"""
     r+ is used for reading and writing. Can not truncate the file.
    w+ is used for writing and reding. Truncates the file i.e. overwrites and deletes all pre-existing data.
    a+ is used for appending and reading. Creates a new file, if none exists.
"""


def clean_files(current_mem, ex_mem):
    with open(current_mem, 'r+') as write_file:  # open file in both read and write mode
        with open(ex_mem, 'a+') as append_file:  # a+ is used for appending and reading. Creates a new file, if none exists.
            # get the data
            write_file.seek(0)
            members = write_file.readlines()
            # remove header  which is: Membership No  Date Joined  Active
            header = members[0]
            members.pop(0)

            # Filter the members left to get those who are inactive
            inactive = [member for member in members if ('no' in member)]  # inactive is a list
            """
                The above comprehension deos the same as the code below:
                for member in members:
                    if 'no' in member:
                        inactive.append(member)
            """
            # Go to the beginning of the write file
            write_file.seek(0)
            write_file.write(header)
            # Now we have two lists i.e. members and inactive.
            # member is a list of all members and inactive is a list of inactive members having "no" in last column.
            for member in members:
                if member in inactive:  # If member, which is in list members, is also on the list of incative.
                    append_file.write(member)
                else:
                    write_file.write(member)

            write_file.truncate()


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
clean_files(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
