import _elementtree
def test():
    parser=_elementtree.XMLParser()
    text='s' * (2**31 + 10)
    try:
        parser.feed(text)
    except OverflowError as err:
        print("ok: %s" % err)
        return
    except:
        pass
    print("error: OverflowError not raised")
test()