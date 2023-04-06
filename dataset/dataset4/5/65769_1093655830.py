import MySQLdb, MySQLdb.cursors, datetime
""" ... mysqlCursor is a cursor object from a connection to database from the MySQLdb module ... """
mysqlCursor.execute("SELECT NOW()")
timeRow = mysqlCursor.fetchall()
currentDateTime = datetime.datetime.strptime(timeRow[0]["NOW()"], "%Y-%m-%d %H:%M:%S")