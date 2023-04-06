def yyy():
    a, b = 'abc', 'abd'
    print([eval(i) for i in ('a', 'b')])


def zzz():
    a, b = 'abc', 'abd'
    print({i: eval(i) for i in ('a', 'b')})


yyy()  # ok
zzz()  # NameError: name 'a' is not defined, however in yyy() it is ok