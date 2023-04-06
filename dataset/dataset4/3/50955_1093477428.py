class SomeServer(asyncore.dispatcher):
    
    ...

    def handle_accept():
       conn = self.accept()
       if conn is None:
           return
       else:
           sock, addr = conn
       ...