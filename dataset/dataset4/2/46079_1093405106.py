def newfilter(flist, skip):
  for pattern in skip:
    flist = list(ifilterfalse(fnmatch.filter(flist,
pattern).__contains__, flist))
  return flist