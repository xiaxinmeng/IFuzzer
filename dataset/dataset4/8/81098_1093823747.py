import ast


class V(ast.NodeVisitor):
    def visit_Str(self, node):
        print(node.s)


def main():
    V().visit(ast.parse('x = "hi"'))


if __name__ == '__main__':
    exit(main())