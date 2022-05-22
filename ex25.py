def break_words(stuff):
    """This function will break words for us."""  # Documentation comments. Try help(ex25) on terminal.
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words that get as arguments."""
    return sorted(words)


def print_first_word(words):
    """Print the first word after popping it off."""
    popped_word = words.pop(
        0)  # The pop() method removes the item at the given index from the list and returns the removed item.
    print(popped_word)


def print_last_word(words):
    """Print the last word after popping it off."""
    popped_word = words.pop(-1)
    print(popped_word)


def sort_sentence(sentence):
    """Takes in a sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    sorted_words = sort_sentence(sentence)
    print_first_word(sorted_words)
    print_last_word(sorted_words)


# Don't add .py to the import statement. Python knows that it is a python file. import ex25 or from ex25 import *
"""
>>> import ex25
>>> help(ex25)
>>> help(ex25.break_words)
>>> sentence = "All good things come to those who work hard while they wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'work', 'hard', 'while', 'they', 'wait.']
>>> type(words)
<class 'list'>
>>> len(words)
12
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'hard', 'they', 'things', 'those', 'to', 'wait.', 'while', 'who', 'work']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
work
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'hard', 'they', 'things', 'those', 'to', 'wait.', 'while', 'who', 'work']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
work
>>>
"""

# Now quit python and start it again but this time use from ex25 import *
"""
>>> from ex25 import *
>>> help(break_words)

>>> sentence = "A quick brown fox jumps over the lazy dog."
>>> words = break_words(sentence)
>>> type(words)
<class 'list'>
>>> len(words)
9
>>> sorted_words = sort_words(words)
>>> sorted_words
['A', 'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the']
>>> words
['A', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
>>> print_first_word(words)
A
>>> print_last_word(words)
dog.
>>> sorted_words = sort_sentence(sentence)
>>> sorted_words
['A', 'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the']
>>> print_first_and_last(sentence)
A
dog.
>>> print_first_and_last_sorted(sentence)
A
the
>>>
"""
