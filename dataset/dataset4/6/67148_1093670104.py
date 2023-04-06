import http.client
import ssl

ssl_context = ssl.create_default_context() 
ssl_context.check_hostname = False
https = http.client.HTTPSConnection(..., context=ssl_context)