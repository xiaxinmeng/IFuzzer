# coding: utf-8
import io
import locale
import os

print ('Local pref: ', locale.getpreferredencoding())
print ('LANG env: ', os.environ['LANG'])

tmpfile = 'ascii.tmp'
fh = io.open(tmpfile, 'wt', encoding='ascii')
fh.write(u'L'*44)
fh.close()
print (io.open(tmpfile).read())

del os.environ['LANG']
print ('Local pref: ', locale.getpreferredencoding())
print ('LANG env has key: ', os.environ.has_key('LANG'))
print( locale.getpreferredencoding())

#This will raise exception
print(io.open(tmpfile).read())
