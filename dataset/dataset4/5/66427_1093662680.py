# -*- encoding: utf-8 -*-
import urllib3
pool_manager = urllib3.PoolManager(num_pools=2)
url = u'http://example.org/form' # removing the 'u' fixes it
content = open('/some/binary/file').read()
fields = [
    ('foo', 'something'),
    ('bar', ('/some/binary/file', content, 'application/octet-stream'))
]
pool_manager.request("POST", url, fields=fields, encode_multipart=True, headers={})