#ZZ = Optional['YY'] 
YY = int

YY = Tuple[Optional[ForwardRef("YY", module=__name__)], int]
print( YY.__args__[0].__args__[0].__forward_module__ )
# this prints __main__ (or whatever __name__ contains)