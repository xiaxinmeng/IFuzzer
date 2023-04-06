import codecs

def search_function(name):
    if name == "myutf8":
        utf8 = codecs.lookup("utf-8")
        utf8_sig = codecs.lookup("utf-8-sig")
        return codecs.CodecInfo(
            name='myutf8',
            encode=utf8.encode,
            decode=utf8_sig.decode,
            incrementalencoder=utf8.incrementalencoder,
            incrementaldecoder=utf8_sig.incrementaldecoder,
            streamreader=utf8_sig.streamreader,
            streamwriter=utf8.streamwriter,
        )


codecs.register(search_function)