from re import *
 
s = 'a->b\na->b\nc->b\nc->b\na->d\na->d\ne->b\ne->b\na->f\na->f\ng->b\ng->b\na->h\na->h\ni->b\ni->b\na->j\na->j\nk->b\nk->b\n'
res = subn(r"(.*\n)(\1)+",r"replaced:\1",s,M)
 
print("output: " + res[0])
print("replace count: %d" % res[1])
 
# if it works right the next print wont show
if res[1] == 8: print("WEIRD: too few replacements ("+str(res[1])+")")