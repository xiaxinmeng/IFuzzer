def make_row_factory(cls_factory, **kw):
    def row_factory(cursor, row, cls=[None]):
        rf = cls[0]
        if rf is None:
            fields = [col[0] for col in cursor.description]
            cls[0] = cls_factory("Row", fields, **kw)
            return cls[0](*row)
        return rf(*row)
    return row_factory

namedtuple_row_factory = make_row_factory(namedtuple)