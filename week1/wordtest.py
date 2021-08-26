import sys
from word import get_plural

def check(word, plural):
    return 1 # if the plural is correct or 0 otherwise.

words = ["beach", "fish", "fox", "bus", "fez", "potato", "fairy", "lady", "boy", "elf", "knife", "fog", "tissue"]

num_correct = 0
for word in words:
    num_correct += check(word, get_plural(word))

print("All Good" if num_correct == len(words) else str(len(words) - num_correct) + " incorrect.")