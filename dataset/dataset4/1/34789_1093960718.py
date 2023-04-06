class Node(object):
   def __int__(self):
      return int(self.str())
   def str(self):
      return "23"

class Frag(Node, list):
   def str(self):
      return "42"