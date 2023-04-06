for i in con.execute('SELECT * FROM table'):
    yield dict2named(i)