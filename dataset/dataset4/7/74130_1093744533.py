class MyList(list):
    def insert(self, index, object):
        super().insert(index, object)

class MyOtherList(list):
    insert = MyList.insert