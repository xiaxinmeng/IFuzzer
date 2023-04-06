# Read and print the values just inserted into tbl
for col in db.execute('SELECT col FROM tbl'):
    print(col)
    db.execute('INSERT INTO tbl2 VALUES (?)', col)
    db.commit()