with open(threadspecific, 'ab') as x:
 txt = unicode(str_or_unicode_parameter).encode('utf8')
 x.write(txt+'\r\n')