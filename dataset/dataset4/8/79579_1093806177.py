
import sqlite3

conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE foo (
    id INTEGER NOT NULL,
    updated_at DATETIME,
    PRIMARY KEY (id)
)
""")

cursor.execute("""
/* watermarking bug */
INSERT INTO foo (id, updated_at) VALUES (?, ?)
""", [1, None])


cursor.execute("""
    UPDATE foo SET updated_at=? WHERE foo.id = ?
""", ('2018-12-02 14:55:57.169785', 1))

assert cursor.rowcount == 1

cursor.execute("""
    /* watermarking bug */
    UPDATE foo SET updated_at=? WHERE foo.id = ?
""", ('2018-12-03 14:55:57.169785', 1))

assert cursor.rowcount == 1
