import ast


class CellVisitor(ast.NodeVisitor):
    def __init__(self):
        self.funcRange = {}
        self.classRange = {}
        self.callname =set()
        self.attrname = set()
        self.allname = set()


    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        funcname = node.name 
        startPos = node.lineno
        endPos = node.end_lineno


        self.funcRange[(funcname,node.lineno,node.col_offset,"function")] = [startPos,endPos]


    def visit_ClassDef(self, node):
        self.generic_visit(node)
        classname = node.name 
        startPos = node.lineno
        endPos = node.end_lineno

        self.classRange[(classname,node.lineno,node.col_offset,"class")] = [startPos,endPos]



    def visit_Attribute(self,node):
        self.generic_visit(node)
        # print(ast.dump(node))
        if isinstance(node.value,ast.Name):
            self.attrname.add((node.value.id,node.lineno,node.col_offset))
            # print(node.value.id,node.lineno,node.col_offset)


    def visit_Name(self, node):
        self.generic_visit(node)

        self.allname.add((node.id,node.lineno,node.col_offset))



    def visit_Call(self, node):
        self.generic_visit(node)
        # print(ast.dump(node))
        if isinstance(node.func, ast.Attribute):
            pass
        else:
            # print(dir(node.func))
            self.callname.add((node.func.id,node.lineno,node.col_offset))





