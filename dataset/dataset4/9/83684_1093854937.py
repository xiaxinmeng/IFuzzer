from urllib.request import AbstractBasicAuthHandler
auth_handler = AbstractBasicAuthHandler()
auth_handler.http_error_auth_reqed(
    'www-authenticate',
    'unused',
    'unused',
    {
        'www-authenticate': 'Basic ' + ',' * 64 + ' ' + 'foo' + ' ' +
'realm'
    }
)