import ast


def getCTX(anode):
    ctx = ""
    if isinstance(anode,ast.Store):
        ctx = "Store"
    if isinstance(anode,ast.Load):
        ctx = "Load"
    if isinstance(anode,ast.Del):    
        # ctx = "Del"
        ctx = "Load"
    return ctx




class CellVisitor(ast.NodeVisitor):
    def __init__(self):
        self.funcRange = {}
        self.funcargs = {}
        self.classRange = {}
        self.callname =set()
        self.calldic = {}
        self.attrname = set()
        self.allname = set()
        self.callarg = set()


    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        funcname = node.name 
        startPos = node.lineno
        endPos = node.end_lineno
        argsNum = 0
        if node.args.args:
            argsNum = len(node.args.args)
            arglist=[]
            for arg in node.args.args:
                arglist.append(arg.arg)

            self.funcargs[(funcname,node.lineno,node.col_offset,argsNum,"function")] = arglist



        self.funcRange[(funcname,node.lineno,node.col_offset,argsNum,"function")] = [startPos,endPos]


    def visit_ClassDef(self, node):
        self.generic_visit(node)
        classname = node.name 
        startPos = node.lineno
        endPos = node.end_lineno
        baseNum = len(node.bases) 

        self.classRange[(classname,node.lineno,node.col_offset,baseNum,"class")] = [startPos,endPos]



    def visit_Attribute(self,node):
        self.generic_visit(node)
        # print(ast.dump(node))
        if isinstance(node.value,ast.Name):
            self.attrname.add((node.value.id,node.lineno,node.col_offset,getCTX(node.ctx)))
            # print(node.value.id,node.lineno,node.col_offset)


    def visit_Name(self, node):
        self.generic_visit(node)

        self.allname.add((node.id,node.lineno,node.col_offset,getCTX(node.ctx)))



    def visit_Call(self, node):
        self.generic_visit(node)
        # print(ast.dump(node))
        if isinstance(node.func, ast.Attribute):
            pass
        else:
            # print(dir(node.func))
            self.callname.add((node.func.id,node.lineno,node.col_offset,getCTX(node.func.ctx)))


            arglist = []
            if node.args:
                for item in node.args:
                    if isinstance(item, ast.Name):
                        self.callarg.add((item.id,item.lineno,item.col_offset,getCTX(item.ctx)))
                        arglist.append((item.id,item.lineno,item.col_offset,getCTX(item.ctx)))


            self.calldic[(node.func.id,node.lineno,node.col_offset,getCTX(node.func.ctx))] = arglist



