def recurse():
    try:raise Exception #An arbitary exception
    except Exception:recurse()