if ")" in rawdata[j:]:
    j = rawdata.find(")", j) + 1
else:
    return -1