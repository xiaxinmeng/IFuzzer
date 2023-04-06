def i():
    yield "line1"
    raise KeyboardInterrupt()

import cStringIO
sio = cStringIO.StringIO()
sio.writelines(i())