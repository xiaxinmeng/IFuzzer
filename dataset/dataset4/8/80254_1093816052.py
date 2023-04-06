import sqlite3 as sqlite
con = sqlite.connect(':memory:', detect_types=sqlite.PARSE_COLNAMES)
cur = con.cursor()
sqlite.converters['CURSOR_INIT'] = lambda x: cur.__init__(con)