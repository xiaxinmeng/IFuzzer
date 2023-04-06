
for word in field:
    sort_tuple = sort_tuple + sort_arg_defs[word][0]
    self.sort_type += connector + sort_arg_defs[word][1]
    connector = ", "
