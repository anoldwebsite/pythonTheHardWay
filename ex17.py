from sys import argv
from os.path import exists

script, from_file, to_file = argv
"""
    
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
"""

open(to_file, 'w').write(open(from_file).read())

"""
    with open(from_file) as f:
    with open(to_file, 'w') as t:
        t.write(f.read())
"""




