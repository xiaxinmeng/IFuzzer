import io, contextlib, logging

message = 'dummy test'

with io.StringIO() as sio:
    with contextlib.redirect_stdout(sio), contextlib.redirect_stderr(sio):
        logging.warning(message)
        output = sio.getvalue()
    print(output)

logging.warning(message)