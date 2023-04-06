from tempfile import NamedTemporaryFile

while 1:
    try:
        NamedTemporaryFile(mode='x')
    except ValueError as ex:
        pass