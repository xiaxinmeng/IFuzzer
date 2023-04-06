class MyFuncs:
    def div(self, x, y) : return div(x,y)


handler = CGIXMLRPCRequestHandler(("localhost", 8000))
handler.register_function(pow)
handler.register_function(lambda x,y: x+y, 'add')
handler.register_introspection_functions()
handler.register_instance(MyFuncs())
handler.handle_request()