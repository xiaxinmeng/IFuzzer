
table = pd.read_sql_query('select * from table', con)
column_type = pd.read_sql_query('PRAGMA table_info("table")', con)['type']
datetimes = table.columns[column_type == 'DATETIME']
table.loc[:, datetimes] = table.loc[:, datetimes].apply(pd.to_datetime)
