import ssl
cert = {'subjectAltName': (('IP Address', '1.1.1.1'),)}
ssl.match_hostname(cert, '1.1.1.1 ; this should not work but does')