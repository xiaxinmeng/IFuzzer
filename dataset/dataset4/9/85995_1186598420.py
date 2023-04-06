class DictRow(dict):
    def __iter__(self):
        return iter(self.values())

def DictRowFactory(cursor, row):
    fields = [i[0] for i in cursor.description]
    return DictRow({k: v for k, v in zip(fields, row)})


cx = sqlite3.connect(':memory:')
cx.row_factory = DictRowFactory