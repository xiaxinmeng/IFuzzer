# Decide if/how we're going to create a hash function.  Key is
#  (unsafe_hash, eq, frozen, does-hash-exist).  Value is the action to
#  take.
# Actions:
#  '':          Do nothing.
#  'none':      Set __hash__ to None.
#  'add':       Always add a generated __hash__function.
#  'exception': Raise an exception.
#
#                +-------------------------------------- unsafe_hash?
#                |      +------------------------------- eq?
#                |      |      +------------------------ frozen?
#                |      |      |      +----------------  has-explicit-hash?
#                |      |      |      |
#                |      |      |      |        +-------  action
#                |      |      |      |        |
#                v      v      v      v        v
_hash_action = {(False, False, False, False): (''),
                (False, False, False, True ): (''),
                (False, False, True,  False): (''),
                (False, False, True,  True ): (''),
                (False, True,  False, False): ('none'),
                (False, True,  False, True ): (''),
                (False, True,  True,  False): ('add'),
                (False, True,  True,  True ): (''),
                (True,  False, False, False): ('add'),
                (True,  False, False, True ): ('exception'),
                (True,  False, True,  False): ('add'),
                (True,  False, True,  True ): ('exception'),
                (True,  True,  False, False): ('add'),
                (True,  True,  False, True ): ('exception'),
                (True,  True,  True,  False): ('add'),
                (True,  True,  True,  True ): ('exception'),
                }