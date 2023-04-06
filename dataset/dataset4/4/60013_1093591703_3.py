pycon
'''
Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
ascii cp1256
ط³ظ„ط§ظ…
سلام
>>> s3 = 'سلام'
>>> s4 = u'سلام'
>>> s3
'\xd3\xe1\xc7\xe3'
>>> s4
u'\u0633\u0644\u0627\u0645'
>>> print s3
سلام
>>> print s4
سلام
>>> s = u'Русский текст'
Unsupported characters in input
'''
