denominations = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four'}
        
def foo(n):
    print('FOO CALLED. n =', n)
    return str(n*10)

words = []
words.append(denominations[1])
words.append(denominations[4])
words.append(denominations.get(1))
words.append(denominations.get(4))
words.append(denominations.get(1, 'ERROR-A'))
words.append(denominations.get(4, 'ERROR-B'))

words.append(denominations.get(22, 'ERROR-1'))
words.append(denominations.get(88, 'ERROR-2'))

words.append(denominations.get(1, foo(1)))
words.append(denominations.get(4, foo(4)))

print(words)



def isItZero(n):
    print('ISITZERO CALLED.  n=', n)
    return False

a = (True or isItZero(9))   # (True or x) is always True so x is not evaluated