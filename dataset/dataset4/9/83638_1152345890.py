# sqlalchemy's sqlite3 isolation level pseudocode
_isolation_lookup = {"READ UNCOMMITTED": 1, "SERIALIZABLE": 0}

def set_isolation_level(self, dbapi_connection, level):
    """set the isolation level for a sqlite3 connection"""

    if level == "AUTOCOMMIT":
        dbapi_connection.isolation_level = None
    else:
        # i believe this is eqvuialent to DEFERRED
        dbapi_connection.isolation_level = ""

        # convert from "READ UNCOMMITTED" or "SERIALIZABLE" to an int
        # read_uncommitted level
        int_level = _isolation_lookup[level]
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA read_uncommitted = %d" % int_level)
        cursor.close()

