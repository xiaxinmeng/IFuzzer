import tokenize
import codecs

with open('text.txt', 'r') as f:
    reader = codecs.getreader('utf-8')(f)
    tokens = tokenize.generate_tokens(reader.readline)