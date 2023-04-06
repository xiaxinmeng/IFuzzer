#!/usr/bin/env python
import shlex

first = shlex.shlex("word1 word2\nword3")
print (first.get_token())
print (first.get_token())
print ("line no", first.lineno)
print ("")

second = shlex.shlex("word1 word2,\nword3")
print (second.get_token())
print (second.get_token())
print (second.get_token())
print ("line no", second.lineno)