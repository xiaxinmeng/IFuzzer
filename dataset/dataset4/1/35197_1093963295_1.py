while 1:
    parser = sax.make_parser()
    parser.setContentHandler(handler.ContentHandler())
    parser.feed("<TEST>hello!</TEST>")