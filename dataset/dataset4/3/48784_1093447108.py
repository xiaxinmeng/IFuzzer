def List_to_String(lis):
#    return str.join(lis, '')		# This is fast, but seems broke in 3.0
    s = ''				# This is really slow, but works in 3.0
    for l in lis: s = s + l
    return s