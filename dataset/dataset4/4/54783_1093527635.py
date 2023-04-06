import re
import email.header

def decodeSafely(x):
    match = re.search('(=\?.*?\?B\?)', x)
    if not match:
        return x
    encoding = match.group(1)
    return email.header.decode_header('%s%s==?=' % (encoding, x.replace(encoding, '').replace('?', '').replace('=', '')))