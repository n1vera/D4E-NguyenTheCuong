from random import shuffle
from random import randint
a = randint(0,4)
wordlist = ['champion',' night',' superman',' ironman']
word = wordlist[a]
b=list(word)
c=shuffle(b)
print(c)
