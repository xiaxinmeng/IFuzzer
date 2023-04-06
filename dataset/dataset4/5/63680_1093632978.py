class S(str):
    def __str__(self):
        return 'S: ' + str.__str__(self)

s = S('foo')
print(s, str(s), str.__str__(s))

import sys
sys.stdout.write(s)