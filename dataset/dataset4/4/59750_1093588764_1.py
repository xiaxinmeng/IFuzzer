class _Row(sqlite3.Row):
    def __lt__(self, x):
        return False