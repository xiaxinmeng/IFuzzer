def write(fp):
    fp.write("""\
a
""")

# eol=0d0a (windows, python-2.6.4)
with open('0d0a.tmp', 'w') as fp:
    write(fp)

# eol=0d0a (windows, python-2.6.4)
with codecs.open('0d0a-codecs.tmp', 'w') as fp:
    write(fp)