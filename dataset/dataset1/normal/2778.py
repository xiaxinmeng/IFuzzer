#!/usr/bin/env python

orig = set('hello')

hashvalue = hash(frozenset(orig))

class BadKey:
    def __hash__(self):
        return hashvalue

    def __eq__(self, other):
        global savedother
        print("In eq orig={0}, other={1}".format(orig, other))
        savedother = other
        return False

s = set([BadKey()])
orig in s
print("After eq orig={0}, other={1}".format(orig, savedother))
