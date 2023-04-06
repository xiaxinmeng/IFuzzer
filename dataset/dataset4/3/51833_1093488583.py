dstr = rfcformat(dt)
if dstr.endswith("-00:00") or dstr.endswith("+00:00"):
    dstr = dstr[:-6] + 'Z'