# /etc/hostname is one line, but our source has multiple lines
code = compile('\n\n\n1/0', '/etc/hostname', 'exec')