import ast
class RewriteName(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id != "print":
            node.id = str(False)
            print(type(node.id))
        return node

code = "a = 2;print(a)"

myast = ast.parse(code)
transformer = RewriteName()
newast = transformer.visit(myast)

c = compile(newast,'','exec')
exec(c)