#At the beginning of peek()
#keep track of prior offset
position = self.fileobj.tell()

#immediately before return statement
#restore previous fileobj offset
self.fileobj.seek(position)