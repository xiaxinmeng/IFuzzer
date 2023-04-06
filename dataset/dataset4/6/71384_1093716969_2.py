# patchbug/b.py
#
from patchbug.a import A

def reference():
    return A().name()

# patchbug/tests.py
#
import mock

"""
patchbug.reference.UnpatchedClass is bound to the value of patchbug.source.UnpatchedClass
at the time of the first import of patchbug.reference. If patched at that time it is not repaired.
"""

def test_unpatched():
    import patchbug.a
    assert patchbug.a.A().name() == "unpatched"

"""
uncommenting the import causes reference.UnpatchedClass to be bound before the patch, fixing
test_reference and breaking test_unpatched
"""
def test_import_reference():
#    import patchbug.b
    pass

def test_patched():
    with mock.patch('patchbug.a.A') as P:
        import patchbug.a, patchbug.b
        P.return_value.name.return_value = "patched"
        assert patchbug.a.A().name() == "patched"
        assert patchbug.b.reference() == "patched"

def test_reference():
    import patchbug.b
    assert patchbug.b.reference() == "unpatched"