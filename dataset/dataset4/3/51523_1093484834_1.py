for passfail in [ "fail" ]:
    cases = [ [( i, open( os.path.join( base, i ), "r").read() )
                for i in files if passfail in i ]
                for base, subs, files in os.walk( "tests" ) ][0]