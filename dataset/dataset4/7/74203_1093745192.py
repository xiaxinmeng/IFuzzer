import io, pprint, zipfile
from zipfile import ZIP_DEFLATED

def printLiteral( data, out ) :
        encoder = io.TextIOWrapper( out, encoding='utf-8', write_through=True )
        pprint.pprint( data, stream=encoder )

data = { 'not' : 'much', 'just' : 'some K \N{RIGHTWARDS WHITE ARROW} V pairs' }

with zipfile.ZipFile( 'zzz.zip', mode='w', compression=ZIP_DEFLATED ) as myzip :

    with myzip.open( 'this one works', 'w' ) as out :
        encoder = io.TextIOWrapper( out, encoding='utf-8', write_through=True )
        pprint.pprint( data, stream=encoder )

    with myzip.open( 'this one fails', 'w' ) as out :
        printLiteral( data, out )

        print( 'printed but entry still open' )
    print( 'entry has been closed but not file' )
print( 'zip file has been closed' )