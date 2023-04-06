class ClassVisitor(ast.NodeVisitor):
    def visit_ClassDef(self, node):
        ...
        if found:
            raise StopIterator(line_number)
        ...
...
try:
    class_visitor.visit(tree)
except StopIterator as e:
    line_number = e.value
else:
    raise OSError('could not find class definition')