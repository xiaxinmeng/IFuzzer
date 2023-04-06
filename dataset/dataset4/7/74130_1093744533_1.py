class MyList(list):
    pass

def insert(self, index, object):
    super().insert(index, object)

MyList.insert = insert