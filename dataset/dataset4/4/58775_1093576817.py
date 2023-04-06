json.dump(obj, fp, 
          skipkeys=False,
          ensure_ascii=True,
          check_circular=True, 
          allow_nan=True,
          cls=None,
          indent=None,
          separators=None,
          default=None, 
          **kw)

json.JSONEncoder(skipkeys=False, 
                 ensure_ascii=True,
                 check_circular=True,
                 allow_nan=True,
                 sort_keys=False,
                 indent=None,
                 separators=None,
                 default=None)