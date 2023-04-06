class ConnectionFixedCtxManager(sqlite3.Connection):
    def __enter__(self) -> ConnectionFixedCtxManager:
        raise Exception(
            "don't use contextmanager on sqlite3 connection, it's broken with isolation_level=None (which is the sane default). use .transaction() instead (see https://github.com/python/cpython/issues/61162)"
        )

    def transaction(self) -> CursorFixedCtxManager:
        return CursorFixedCtxManager(self)


class CursorFixedCtxManager(ContextManager[sqlite3.Cursor]):
    _cursor: sqlite3.Cursor | None = None

    def __init__(self, conn: ConnectionFixedCtxManager):
        self._conn = conn

    def __enter__(self) -> sqlite3.Cursor:
        self._cursor = self._conn.cursor()
        self._cursor.execute("BEGIN")
        return self._cursor

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        assert self._cursor
        if exc_type is None:
            self._conn.commit()
        else:
            self._conn.rollback()
        self._cursor.close()
        self._cursor = None