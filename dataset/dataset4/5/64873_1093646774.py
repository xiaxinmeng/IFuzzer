pycon
"""
/*                                                                                                                                
Major subtleties ahead:  Most hash schemes depend on having a "good" hash                                                         
function, in the sense of simulating randomness.  Python doesn't:  its most                                                       
important hash functions (for strings and ints) are very regular in common                                                        
cases:                                                                                                                            
                                                                                                                                  
  >>> map(hash, (0, 1, 2, 3))                                                                                                     
  [0, 1, 2, 3]                                                                                                                    
  >>> map(hash, ("namea", "nameb", "namec", "named"))                                                                             
  [-1658398457, -1658398460, -1658398459, -1658398462]                                                                            
  >>>                                                                                                                             
                                                                                                                                  
This isn't necessarily bad!  To the contrary, in a table of size 2**i, taking                                                     
the low-order i bits as the initial table index is extremely fast, and there                                                      
are no collisions at all for dicts indexed by a contiguous range of ints.                                                         
The same is approximately true when keys are "consecutive" strings.  So this                                                      
gives better-than-random behavior in common cases, and that's very desirable. 
"""
