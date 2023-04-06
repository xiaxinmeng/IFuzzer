import lxml
import lxml.etree

with open('test.xml', 'rb') as f:
    list(
        lxml.etree.iterparse(f)
    )

    # Traceback (most recent call last):
    # File "test.py", line 18, in <module>
    # lxml.etree.iterparse(f)
    # File "src/lxml/iterparse.pxi", line 209, in lxml.etree.iterparse.__next__
    # File "src/lxml/iterparse.pxi", line 194, in lxml.etree.iterparse.__next__
    # File "src/lxml/iterparse.pxi", line 225, in lxml.etree.iterparse._read_more_events
    # File "src/lxml/parser.pxi", line 1380, in lxml.etree._FeedParser.close
    # Segmentation fault
    list(
        lxml.etree.iterparse(f)
    )