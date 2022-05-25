import string
from decimal import Decimal


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("OR, we can use variable from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too.")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("****************************************************")
print(isinstance("Dilshad Rana", str))  # True
print(isinstance(65, str))  # False
print(isinstance("65", str))  # True
print(isinstance(65, float))  # False
print(isinstance(65, int))  # True
print("****************************************************")

x = Decimal(2.34)
print(type(x))
print(x * 2)
print(type(x))

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
    "Freecodecamp has great coding tutorials. #skillup",
    " I am excited to test this program on a lot of tweets."
]
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']
"""
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
"""

print("****************************************************")
num_happy_tweet = 0
num_sad_tweet = 0
num_neutral_tweet = 0

for tweet in tweets:
    tweets_without_punc = tweet.translate(str.maketrans('', '', string.punctuation))
    words = tweets_without_punc.split(" ")

    break_taken = False

    for word in words:
        if word in happy_words:
            num_happy_tweet += 1
            break_taken = True
            break
        elif word in sad_words:
            num_sad_tweet += 1
            break_taken = True
            break

    if not break_taken:
        num_neutral_tweet += 1

print(f"Number of happy tweets: {num_happy_tweet}")
print(f"Number of sad tweets: {num_sad_tweet}")
print(f"Number of neutral tweets: {num_neutral_tweet}")

print("********************************************************")


def classify_tweets(tweets_array, happy_array, sad_array):
    happy_tweets = []
    sad_tweets = []
    neutral_tweets = []

    for tweet in tweets_array:
        t = tweet.translate(str.maketrans('', '', string.punctuation))  # tweet without punctuation.
        words = t.split(" ")
        for word in words:
            if word in happy_array:
                happy_tweets.append(tweet)
                break
            if word in sad_array:
                sad_tweets.append(tweet)
                break

        if tweet not in happy_tweets and tweet not in sad_tweets:
            neutral_tweets.append(tweet)

    return len(happy_tweets), len(sad_tweets), len(neutral_tweets)


num_happy_tweet, num_sad_tweet, num_neutral_tweet = classify_tweets(tweets, happy_words, sad_words)

print(f"Number of happy tweets: {num_happy_tweet}")
print(f"Number of sad tweets: {num_sad_tweet}")
print(f"Number of neutral tweets: {num_neutral_tweet}")
print("*****************************************************")


def classify_tweets2(tweets_array, happy_array, sad_array):
    num_happy = 0
    num_sad = 0
    num_neutral = 0
    tweets_decided = 0
    iteration_num = 0
    for tweet in tweets_array:
        iteration_num += 1
        t = tweet.translate(str.maketrans('', '', string.punctuation))  # tweet without punctuation.
        words = t.split(" ")
        for word in words:
            if word in happy_array:
                num_happy += 1
                tweets_decided += 1
                break
            if word in sad_array:
                num_sad += 1
                tweets_decided += 1
                break
        if iteration_num != tweets_decided:
            num_neutral += 1
            tweets_decided += 1

    return num_happy, num_sad, num_neutral


num_happy_tweet, num_sad_tweet, num_neutral_tweet = classify_tweets2(tweets, happy_words, sad_words)

print(f"Number of happy tweets: {num_happy_tweet}")
print(f"Number of sad tweets: {num_sad_tweet}")
print(f"Number of neutral tweets: {num_neutral_tweet}")
