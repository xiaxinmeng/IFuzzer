import ast

# #changelist: [("a",1,2),("b",2,3)]
class Transformer(ast.NodeTransformer):
    def __init__(self,changelist):
        self.changelist = changelist




    def visit_Name(self, node): 
        self.generic_visit(node)
        for item in self.changelist:
          changeid = item[0]
          changelineno = item[1]
          changecol_offset = item[2]
          if node.lineno == changelineno and node.col_offset == changecol_offset:
              node.id = changeid
        
        return node


def transform(translist,myast):
    trans = Transformer(translist)
    newast = trans.visit(myast)
    program = ast.unparse(newast)
    return program