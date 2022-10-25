# There are so many libaries in python.

# random library comes python by defualt.

# For more details Visit (docs.python.org/3/library/random.html)

# random module contain somany function.
# using random.choice function to flip a coin
import random
from secrets import choice
# random.choice(seq) takes seq like ex: lists,.....
coin  = random.choice(["head","tail"])
print(coin)

# you can importing only choice function by from keyword
from random import choice
# so we need not to specify random.choice
coin = choice(["head","tail"])
print(coin)

# Now another function in in random module.(random.randint(a,b))

import random
# Here range from 1 to 6
number = random.randint(1,6)
print(number)


# Now another function in in random module.(random.shuffle(x))

import random

cards = ["king","queen","jack","joker"]
random.shuffle(cards)
for card in cards:
    print(card)

# python another library(statics)
# for more details Visit(docs.python.org/3/library/statistics.html)

import statistics

mean = statistics.mean([100,98,99,22])
print(mean)