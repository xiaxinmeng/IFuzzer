
import sqlite3 as sqlite

if __name__ == '__main__':
    conn = sqlite.connect(":memory:")
    conn.executescript("""
        CREATE TABLE t(c);
        INSERT INTO t VALUES(0);
        INSERT INTO t VALUES(1);
        INSERT INTO t VALUES(2);
    """)

    curs = conn.cursor()
    curs.execute("BEGIN TRANSACTION")
    curs.execute("SELECT c FROM t WHERE ?", (1,))
    conn.rollback()

    # Reusing the same statement from the statement cache, which has been
    # reset by the rollback above.
    gen = conn.execute("SELECT c FROM t WHERE ?", (1,))

    # Any of the following will cause a spurious reset of the statement.
    curs.close()
    # curs.execute("SELECT 1")
    # del curs

    # Expected output: [(0,), (1,), (2,)]
    # Observed output: [(0,), (0,), (1,), (2,)]
    print(list(gen))

    # Raises `sqlite3.InterfaceError: Error binding parameter 0 - probably unsupported type.`
    conn.execute("SELECT c FROM t WHERE ?", (1,))
