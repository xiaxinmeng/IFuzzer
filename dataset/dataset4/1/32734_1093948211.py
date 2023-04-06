import string
import pre as re
pat = re.compile('(^    [^\n]+\n)+', re.MULTILINE)
str = 17365 * ( '     ' + 'tcagtcagtg ' * 6 + '\n' )
pat.search( str )