# Match encoded-word strings in the form =?charset?q?Hello_World?=                       
ecre = re.compile(r'''                                                                   
  =\?                   # literal =?                                                     
  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset                     
  \?                    # literal ?                                                      
  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive                        
  \?                    # literal ?                                                      
  (?P<encoded>.*?)      # non-greedy up to the next ?= is the encoded string             
  \?=                   # literal ?=                                                     
  ''', re.VERBOSE | re.IGNORECASE | re.MULTILINE)