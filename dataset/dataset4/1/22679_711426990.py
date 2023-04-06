import random
from string import ascii_uppercase as alphabet
zipf = [1/x for x in range(1, 1+26)]

def zipf_string(length):
    letters = random.choices(alphabet, weights=zipf, k=length)
    return ''.join(letters)