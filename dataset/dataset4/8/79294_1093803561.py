import ast
import inspect


class MyClassVisitor(ast.NodeVisitor):

    def __init__(self, lines, *args, **kwargs):
        self.lines = lines
        super().__init__(*args, **kwargs)

    def visit_ClassDef(self, node):
        print('Found class "%s"' % node.name)
        print("Source")
        print(''.join(inspect.getblock(self.lines[node.lineno-1:])))

with open('../backups/bpo35101_1.py') as f:
    source = f.read()
    lines = source.splitlines(True)
    tree = ast.parse(source)
    MyClassVisitor(lines).visit(tree)