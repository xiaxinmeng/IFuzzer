locatestarttagend = re.compile(r"""
  <[a-zA-Z][-.a-zA-Z0-9:_]*          # tag name
  \s*                                # whitespace after tag name
  (?:
    (?:[a-zA-Z_][-.:a-zA-Z0-9_]*     # attribute name
      (?:\s*=\s*                     # value indicator
        (?:'[^']*'                   # LITA-enclosed value
          |\"[^\"]*\"                # LIT-enclosed value
          |[^'\">\s]+                # bare value
         )?
       )?
     )
     \s*                             # whitespace between attrs
   )*
  \s*                                # trailing whitespace
""", re.VERBOSE)