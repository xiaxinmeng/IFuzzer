# ftrlist is the stuff I *want* to keep: 
ftrlist = [re.escape(i) for i in ftrlist ]
re.compile(r'(?!(%s))'  %( '|'.join(ftrlist)) )
#