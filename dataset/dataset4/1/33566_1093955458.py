while 1:
    gota = a.popitem()
    gotb = b.popitem()
    assert gota == gotb, (gota, gotb, len(a), len(b))