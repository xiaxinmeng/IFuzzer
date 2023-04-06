os.rename('/dev/foobar', '/dev/barfoo') # fails because /dev/foobar doesn't exist

os.rename('/dev/null', '/foo/bar/baz') # fails because /foo/bar doesn't exist