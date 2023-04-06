class ClassVisitor(ast.NodeVisitor):

    def recursive(func):
        """ decorator to make visitor work recursive """
        def wrapper(self, node):
            func(self, node)
            for child in ast.iter_child_nodes(node):
                self.visit(child)
        return wrapper

    def __init__(self, source, name, *args, **kwargs):
        self.source = source
        self.line_number = None
        self.name = name
        super().__init__(*args, **kwargs)

    @recursive
    def visit_ClassDef(self, node):
        # Need to match qualified name to differentiate between Spam and NestedA.Spam
        if node.name == self.name:
            # decrement by one since lines list starts with indexing by zero
            self.line_number = node.lineno - 1

name = object.__name__ # can use object.__qualname__ but node.name is not qualified
source = ''.join(lines)
tree = ast.parse(source)
class_visitor = ClassVisitor(source, name)
class_visitor.visit(tree)

if class_visitor.line_number is not None:
    return lines, class_visitor.line_number
else:
    raise OSError('could not find class definition')