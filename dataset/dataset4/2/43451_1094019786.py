import re
literal = r'e:\prg\vc\1'
assert re.sub( '(a+)', 
               literal.replace('\\','\\\\'), 
               'aabac' ) == (literal+'b'+literal+'c')