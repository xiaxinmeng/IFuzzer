ast.literal_eval("'%s'" % e)
e.encode().decode('unicode-escape').encode('latin1').decode()
e.encode('latin1', 'backslashescape').decode('unicode-escape')