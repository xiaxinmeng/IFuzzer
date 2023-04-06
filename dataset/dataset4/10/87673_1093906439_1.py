def foo():
     mstr = "s=1"
     exec(compile(mstr,'','exec'))
     print(s)
foo()