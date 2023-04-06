locatestarttagend_tolerant = re.compile(r"""
  <[a-zA-Z][-.a-zA-Z0-9:_]*          # tag name
  (?:(?:\s+|(\s*))                   # optional whitespace before attribute name
    (?:[a-zA-Z_][-.:a-zA-Z0-9_]*     # attribute name
      (?:\s*=\s*                     # value indicator
        (?:'[^']*'                   # LITA-enclosed value
          |\"[^\"]*\"                # LIT-enclosed value
          |[^'\">\s]+                # bare value
         )
         (?:\s*(,))*                   # possibly followed by a comma
       )?
     )
   )*
  \s*                                # trailing whitespace
""", re.VERBOSE)
attrfind_tolerant = re.compile(
    r'\s*([a-zA-Z_][-.:a-zA-Z_0-9]*)(\s*=\s*'
    r'(\'[^\']*\'|"[^"]*"|[^>\s]*))?')