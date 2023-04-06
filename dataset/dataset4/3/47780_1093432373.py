import ast
a = ast.parse('foo', mode='eval')
x = compile(a, '<unknown>', mode='eval')

class RewriteName(ast.NodeTransformer):
    def visit_Name(self, node):
        return ast.Subscript(
            value=ast.Name(id='data', ctx=ast.Load()),
            slice=ast.Index(value=ast.Str(s=node.id)),
            ctx=node.ctx
        )

a2 = ast.fix_missing_locations(RewriteName().visit(a))