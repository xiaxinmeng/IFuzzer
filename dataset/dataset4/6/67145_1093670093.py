class PreparedStatement(object):
    def __init__(self, connection, statement):
        self.cursor = connection.cursor(prepared=True)
        self.statement = statement

    def execute(self, params):
        self.cursor.execute(self.statement, params)

    def fetchall(self):
        return self.cursor.fetchall()