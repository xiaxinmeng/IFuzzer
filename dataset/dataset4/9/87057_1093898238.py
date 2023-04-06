from lsm import LSM


db = LSM('db.sqlite')


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    global db
    for (index, (key, value)) in enumerate(db[b'\x00':b'\xFF']):
        pass