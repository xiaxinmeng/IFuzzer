pat = re.compile(...)
if type(pat) is types.InstanceType:
    pattern_type = pat.__class__
else:
    pattern_type = type(pat)