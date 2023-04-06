import os
import tempfile

want_to_replace = 'zxc.dat'
tmpdir=os.path.dirname(os.path.realpath(want_to_replace))
with tempfile.NamedTemporaryFile(dir=tmpdir) as fff:
    # do somewhat with fff here... and then:
    fff.flush()
    os.fdatasync(fff)
    os.rename(fff.name, want_to_replace)
    fff.delete = False