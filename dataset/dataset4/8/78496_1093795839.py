import re

regex = r'DELETE\s*(?P<table_alias>[a-zA-z_0-9]*)\s*FROM\s*(?P<table_name>[a-zA-z_0-9]+)\s*([a-zA-Z0-9_]*)\s*(?P<where_statement>WHERE){0,1}(\s.)*?'

test_str = 'DELETE FROM my_table1 t_ WHERE id in (1,2,3)'

matches = re.finditer(regex, test_str, re.MULTILINE)