# extract good value from JSON object
cursor.execute("""
    SELECT JSON_EXTRACT(some_data.data, '$."foo"')
    FROM some_data WHERE id=1
""")
assert cursor.fetchone()[0] == good_data

# extract bad value from JSON object; utf-8 failure
# sqlite3.OperationalError: Could not decode to UTF-8 column
# 'JSON_EXTRACT(some_data.data, '$."foo"')' with text 'r��ve������ ill��'
cursor.execute("""
    SELECT JSON_EXTRACT(some_data.data, '$."foo"')
    FROM some_data WHERE id=2
""")
assert cursor.fetchone()[0] == bad_data