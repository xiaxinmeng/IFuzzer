import sys
import datetime
import sqlite3
import traceback
import contextlib


def main():
    db = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES)
    db.executescript("""
        CREATE TABLE IF NOT EXISTS test (
            timestamp TIMESTAMP)
        """)

    t = datetime.datetime.now(tz=datetime.timezone.utc)
    t = t.replace(microsecond=0)
    db.executemany("INSERT INTO test VALUES (:timestamp)", [{'timestamp': t}])
    db.commit()

    with contextlib.closing(db.cursor()) as c:
        try:
            c.execute('SELECT * FROM test')
            c.fetchall()
            print('original implementation success')
        except Exception as e:
            print('original implementation failed')
            traceback.print_exc()
        c.close()

    sqlite3.register_converter("timestamp", _sqlite_convert_timestamp)

    with contextlib.closing(db.cursor()) as c:
        try:
            c.execute('SELECT * FROM test')
            c.fetchall()
            print('patched implementation success')
        except Exception as e:
            print('patched implementation failed')
            traceback.print_exc()
        c.close()


def _sqlite_convert_timestamp(val):
    datepart, timepart = val.split(b" ")

    # this is the patch
    timepart = timepart.split(b'+', 1)[0].split(b'-', 1)[0]