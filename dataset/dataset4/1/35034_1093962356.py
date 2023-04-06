gunk = 'xyzzy'

def func():
    global gunk

    junk = 'plugh'
    exec('gunk = junk')