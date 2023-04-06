kxroberto.seek(nrBytes)
assert kxroberto.readline() == """\
To redirect POST as GET _while_ simply loosing (!) the data
(and not appending it to the GET-URL) is most bad for a lib."""