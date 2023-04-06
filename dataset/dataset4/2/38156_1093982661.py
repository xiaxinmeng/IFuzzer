#foobar.py
def open(filename, flag='c'):
    import dumbdbm
    return dumbdbm.open(filename,flag)

c=open('test.dbm')

#main.py
import foobar