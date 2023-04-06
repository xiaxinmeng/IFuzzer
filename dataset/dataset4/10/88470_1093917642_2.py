class OuterConnectionWrapper:
    def __init__(self, connection):
        self.connection = connection

    def go(self, stmt):
        sqlite_connection = self.connection
        cursor = sqlite_connection.cursor()
        cursor.execute("select 1")
        return cursor

    def execute(self, stmt):
        return greenlet_spawn(self.go, stmt)

    def _do_close(self):
        self.connection.close()
        self.connection = None

    def close(self):
        self._do_close()


class InnerConnectionWrapper:
    def __init__(self, connection):
        self.connection = connection

    def create_function(self, *arg, **kw):
        self.connection.create_function(*arg, **kw)

    def cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection = None


class ConnectionPool:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")

        def regexp(a, b):
            return None

        self.conn.create_function("regexp", 2, regexp)

    def connect(self):
        return InnerConnectionWrapper(self.conn)


def do_test():
    pool = ConnectionPool()

    def go():
        c1 = pool.connect()
        conn = OuterConnectionWrapper(c1)
        try:
            conn.execute("test")
        finally:
            conn.close()

    _expect_raises_fn(go)


do_test()