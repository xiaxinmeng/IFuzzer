tbl="""\
create table test1 (
        db_insert_date       timestamp,
        check( cast(substr(db_insert_date,1,4) as integer) >= 2000 and cast(substr(db_insert_date,1,4) as integer) <= 2025),
        check( cast(substr(db_insert_date,6,2) as integer) >= 1    and cast(substr(db_insert_date,6,2) as integer) <= 12),
        check( cast(substr(db_insert_date,9,2) as integer) >= 1    and cast(substr(db_insert_date,9,2) as integer) <= 31)
)
"""

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute(tbl)

query = "insert into test1 values( ? )"
c.execute(query, ("2012-08-20", ) )
conn.commit() # this works