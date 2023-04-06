Nt = namedtuple('LessFields', 'f1 f3')
nt = Nt(f1='one', f2=2)

mywriter.writerow(nt) # writes one,missing,2