def tearDown():
    patch.stopall()

def test123():
    p=patch.dict(...)
    p.start()
    assert False
    p.stop()