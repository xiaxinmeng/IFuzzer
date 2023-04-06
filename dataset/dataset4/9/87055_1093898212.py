import ast
class RewriteName(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if node.left.value == 1:
            node.left = node
        return node

code = """
mystr  = 1 + (2+3)
"""

myast = ast.parse(code)

transformer = RewriteName()
newast = transformer.visit(myast)

c = compile(newast,'<test>','exec')
exec(c)