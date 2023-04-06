import re

splitter = re.compile( r'(\s*[+/&;,]\s*)|(\s+and\s+)' )
ll = splitter.split( 'Dave & Sam, Jane and Zoe' )
print(repr(ll))

print( 'Try again with revised RegEx' )
splitter = re.compile( r'(?:(?:\s*[+/&;,]\s*)|(?:\s+and\s+))' )
ll = splitter.split( 'Dave & Sam, Jane and Zoe' )
print(repr(ll))