import selectors
import tempfile
import traceback

sel = selectors.EpollSelector()

with tempfile.TemporaryFile() as f:
    try:
        sel.register(f, selectors.EVENT_READ)
    except PermissionError:
        traceback.print_exc()
    print("This should have raised a KeyError:", sel.get_key(f))