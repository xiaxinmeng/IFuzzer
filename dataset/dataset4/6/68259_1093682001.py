data = re.sub(r'#.*', '', text, re.MULTILINE) # fails

data = re.sub(r'(?m)#.*', '', text) # Ok
data = re.sub(r'#.*', '', text, re.MULTILINE|re.DEBUG) # Ok