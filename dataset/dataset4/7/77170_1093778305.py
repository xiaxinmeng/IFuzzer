# Find what looks like the start of a popular statement.
_synchre = re.compile(r"""
    ^
    [ \t]*
    (?: while
    |   else
    |   def
    |   return
    |   assert
    |   break
    |   class
    |   continue
    |   elif
    |   try
    |   except
    |   raise
    |   import
    |   yield
    )
    \b
""", re.VERBOSE | re.MULTILINE).search