class JsonMatcher(object):
   def __init__(self, expected):
       self.expected = expected

   def __eq__(self, other):
       return json.loads(other) == self.expected