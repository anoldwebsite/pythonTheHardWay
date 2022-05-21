# \t for tab
tabby_cat = "\tI'm tabbed in."
# \n for new line
persian_cat = "I'm split\non a line."
# \\ one backslash is the escape sequence and the other is the character backslash that we want to print.
backlash_cat = "I'm \\a \\cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

print("""
Hi 'Dilshad'
Hello "Rana"
""")

print('''
Hi "Dilshad"
Hello 'Rana'
''')

print("""
\\\\ \t backslash(\\)
\\\' \t single quotes(')
\\\" \t double quotes(')
\\a \t ASCII bell (BEL)
\\b \t ASCII backspace(BS)
\\f \t ASCII formfeed(FF)
\\n \t ASCII linefeed(LF)
\\N{name} \t Character named name in the Unicode database (Unicode only)
\\r \t Carriage return (CR)
\\t \t Horizontal tab(TAB)
\\uxxxx \t Character with 16-bit hex value xxxx
\\uxxxxxxxx \t Character with 32-bit hex value xxxxxxxx
\\v \t ASCII vertical tab (VT)
\\000 \t Character with octal value ooo
\\xhh \t Character with hex value hh

""")