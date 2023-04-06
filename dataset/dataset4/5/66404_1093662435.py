metadata = TarInfo.make_file('helloworld.txt', len(b))
tarFileObj.addfile(metadata, io.BytesIO(b))