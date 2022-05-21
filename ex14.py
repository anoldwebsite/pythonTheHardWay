# Run this code from commandline using the command: python3 ex14.py Dilshad
from sys import argv

script, user_name = argv

prompt = ':> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)
user_name = "Dilshad"
prompt = '>'
print(f"What kind of computer do you have {user_name}?")
computer = input(prompt)

reply = """
Alright, so you said {} about liking me.
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
"""

to_print = reply.format(likes, lives, computer)
print(to_print)

"""
ToD0#
    Try with a different prompt than the one above.
    Get the error ValueError: need more than 1 value to unpack.”

"""