def enum(*valuenames):
     return namedtuple('Enum', valuenames)(*range(len(valuenames)))