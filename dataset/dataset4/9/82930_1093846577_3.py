# we can retrieve the JSON objects as a whole from the DB, no issue
cursor.execute("SELECT some_data.data FROM some_data ORDER BY id")
assert cursor.fetchall() == [(good_data_json, ), (bad_data_json, )]