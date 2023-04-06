import ast

# #changelist: [("a",1,2),("b",2,3)]
class Transformer(ast.NodeTransformer):
    def __init__(self,changelist,callname):
        self.changelist = changelist
        self.callname = callname
        self.calllist = []
        self.namedic = {}
        self.calldic = {}



    def handle_call(self):
        for item in self.callname:
            self.calllist.append((item[1],item[2]))

        for item in self.changelist:
            postup = (item[1],item[2])
            if postup in self.calllist:
              self.calldic[postup] = item[0]

            else:
              self.namedic[postup] =item[0]

        # print(self.calldic,self.namedic)

    def visit_Call(self, node): 
        # self.generic_visit(node)
        # print("kkkkkkkkkkkkkkkkkk")
        # self.handle_call()
        # print(node.lineno,node.col_offset)
        if isinstance(node.func, ast.Attribute):
            pass
        else:
          # print(node.lineno,node.col_offset,self.calllist,ast.dump(node))
          # print(self.changelist)
          postup = (node.lineno,node.col_offset)
          if postup in self.calldic:
            # print(ast.unparse(ast.parse(self.calldic[postup]).body[0].value))
            node = ast.parse(self.calldic[postup]).body[0].value


          # for item in self.changelist:
          #   changeid = item[0]
          #   changelineno = item[1]
          #   changecol_offset = item[2]
          #   if node.lineno == changelineno and node.col_offset == changecol_offset and (node.lineno,node.col_offset) in self.calllist:

          #       changeast = ast.parse(changeid)
          #       print(ast.dump(changeast))
          #       print(ast.dump(changeast.body[0].value))
          #       print(ast.dump(node))
          #       # node = node
          #       node = changeast.body[0].value
        self.generic_visit(node)
        return node

    def visit_Name(self, node): 
        self.generic_visit(node)  
        # self.handle_call()
        postup = (node.lineno,node.col_offset)
        # print(postup)
        # print(self.calldic.keys())
        if postup in self.namedic.keys():
          # print(self.namedic[postup])
          if "(" in self.namedic[postup]:
            # print(postup)
            node = ast.parse(self.namedic[postup]).body[0].value
          else:
            node.id = self.namedic[postup]
          # node = ast.parse(self.calldic[postup]).body[0].value

        # for item in self.changelist:
        #   changeid = item[0]
        #   changelineno = item[1]
        #   changecol_offset = item[2]
        #   if node.lineno == changelineno and node.col_offset == changecol_offset and "(" not in changeid:
        #       node.id = changeid
        # self.generic_visit(node)
        return node







    # def visit_Call(self, node):
    #     self.generic_visit(node)
    #     # print(ast.dump(node))
    #     if isinstance(node.func, ast.Attribute):
    #         pass
    #     else:
    #         # print(dir(node.func))
    #         self.callname.add((node.func.id,node.lineno,node.col_offset,getCTX(node.func.ctx)))


    #         arglist = []
    #         if node.args:
    #             for item in node.args:
    #                 if isinstance(item, ast.Name):
    #                     self.callarg.add((item.id,item.lineno,item.col_offset,getCTX(item.ctx)))
    #                     arglist.append((item.id,item.lineno,item.col_offset,getCTX(item.ctx)))


    #         self.calldic[(node.func.id,node.lineno,node.col_offset,getCTX(node.func.ctx))] = arglist




def transform(translist,myast):
    trans = Transformer(translist)
    newast = trans.visit(myast)
    program = ast.unparse(newast)
    return program


# class Transformer(ast.NodeTransformer):
#     def __init__(self,changedic,readlist,writelist,calllist):
#         self.changedic = changedic


#     def visit_Name(self, node): 
#         self.generic_visit(node)
#         # print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
#         # print(node.id,node.lineno,node.col_offset,'sssssssssss')
#         postuple = (node.id, node.lineno, node.col_offset)
#         if  postuple in self.readlist or postuple in self.writelist and postuple not in self.calllist :
#             # print("hhhhhhhhhhhhhhhh")

#             if isinstance(self.changedic[postuple],tuple):
#                 if self.changedic[postuple][1]:
#                     func =self.changedic[postuple][0] +'(' + ','.join(list(self.changedic[postuple][1]))+')'
#                 else:
#                     func = self.changedic[postuple][0] + '('+')'

#                 node = ast.parse(func).body[0].value
            

#             else:            


#                 node.id = self.changedic[postuple]
        
#         return node

#     def visit_Call(self, node): 
#         # self.generic_visit(node)
#         # print("kkkkkkkkkkkkkkkkkk")
#         if isinstance(node.func, ast.Attribute):
#             pass
#         else:

#             postuple = (node.func.id,node.lineno,node.col_offset)
#             # print(postuple,"kkkkkkkkkkkkkkkkkk")
#             if postuple in self.calllist:
#                 # print("llllllllllllll")
#                 if isinstance(self.changedic[postuple],tuple):
#                     if self.changedic[postuple][1]:
#                         func =self.changedic[postuple][0] +'(' + ','.join(list(self.changedic[postuple][1]))+')'
#                     else:
#                         func = self.changedic[postuple][0] + '('+')'


#                     node = ast.parse(func).body[0].value
#                 else:
#                     node = ast.parse(self.changedic[postuple]).body[0].value
#         self.generic_visit(node)
#         return node

