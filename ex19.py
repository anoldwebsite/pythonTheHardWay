import string


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("OR, we can use variable from our scripts:")
amouunt_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amouunt_of_cheese, amount_of_crackers)

print("We can even do math inside too.")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amouunt_of_cheese + 100, amount_of_crackers + 1000)

print("****************************************************")
print(isinstance("Dilshad Rana", str))  # True
print(isinstance(65, str))  # True
print(isinstance(65, float))  # True
print(isinstance(65, int))  # True
print("****************************************************")
from decimal import Decimal

x = Decimal(2.34)
print(type(x))
print(x * 2)

y = 2.34
print(type(y))
print(y * 2)
print("****************************************************")
# Identity operators is / is not
x = None
print(x is None)  # True

is_open = True
print(is_open is True)  # True

is_open = False
print(is_open is not True)  # True
print("****************************************************")
x = True
print(-x)
x = 2
print(-x)
x = 4.5
print(-x)
print("Learning with INE" not in "Learning Python with INE")  # True
my_variable = "James" * 2 * 3

print(my_variable)
print("****************************************************")
file_lines = None
file_words = None

with open("members.txt", "r") as file:
    lines_count = 0
    words_count = 0

    for line in file:
        if line != "\n":
            lines_count += 1
            words_count += len(line.split(" "))

    file_lines = lines_count
    file_words = words_count

print(f"Lines in file: {file_lines}")
print(f"Words in file: {file_words}")
print("****************************************************")

print("****************************************************")
tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

# store the final answer in this variable
number_of_neutral_tweets = 0

# perform the calculation here

import string

for tweet in tweets:
    neutral = True

    tweet_without_punctuations = tweet.translate(str.maketrans('', '', string.punctuation))
    tweet_chunks = tweet_without_punctuations.split(" ")
    for word in tweet_chunks:
        if word in happy_words or word in sad_words:
            neutral = False
            break

    if neutral:
        number_of_neutral_tweets += 1
        print(f"'{tweet}' is neutral.")


print(number_of_neutral_tweets)

print("****************************************************")
