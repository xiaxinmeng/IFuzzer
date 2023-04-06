from lsm import LSM


db = LSM('db.sqlite')

def app(environ, start_response):
    """Simplest possible application object"""

    for (index, (key, value)) in enumerate(db[b'\x00':b'\xFF']):
        pass

    start_response(b'200', {})
    return b''

db.close()