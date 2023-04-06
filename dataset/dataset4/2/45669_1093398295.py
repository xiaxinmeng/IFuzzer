import codecs

def search_function(name):
    if name == "myutf8":
        utf8 = codecs.lookup("utf-8")
        utf8_sig = codecs.lookup("utf-8-sig")
        return codecs.CodecInfo(
            name='myutf8',
            encode=utf8.encode,
            decode=utf8_sig.decode,
            incrementalencoder=utf8.IncrementalEncoder,
            incrementaldecoder=utf8_sig.IncrementalDecoder,
            streamreader=utf8_sig.StreamReader,
            streamwriter=utf8.StreamWriter,
        )


codecs.register(search_function)