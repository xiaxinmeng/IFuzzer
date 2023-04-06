def _Suite(self, tree):
      for stmt in tree.body:
         self.dispatch(stmt)