def unquote(str):
    """Remove quotes from a string."""
    if len(str) > 1:
        if str.startswith('"'):
          if str.endswith('"'):
            str = str[1:-1]
          else: # remove garbage after trailing quote
            try: str = str[1:str[1:].index('"')+1]
            except: return str
          return str.replace('\\\\', '\\').replace('\\"', '"')
        if str.startswith('<') and str.endswith('>'):
            return str[1:-1]
    return str