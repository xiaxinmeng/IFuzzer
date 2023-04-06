from urllib.request import AbstractBasicAuthHandler
auth_handler = AbstractBasicAuthHandler()
header = {'www-authenticate': 'Basic ' + ',' * 64 + ' ' + 'foo' + ' ' +'realm'}
auth_handler.http_error_auth_reqed('www-authenticate','unused','unused',header)