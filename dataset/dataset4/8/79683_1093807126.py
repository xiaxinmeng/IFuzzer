import gc
from io import StringIO
import xml.etree.ElementTree as etree

import objgraph


def parse_xml():
    xml = """
      <LEVEL1>
      </LEVEL1>
    </ROOT>
    """
    parser = etree.iterparse(StringIO(initial_value=xml))
    for _, elem in parser:
        if elem.tag == 'LEVEL1':
            break


def run():
    parse_xml()

    gc.collect()
    uncollected_elems = objgraph.by_type('Element')
    print(uncollected_elems)
    objgraph.show_backrefs(uncollected_elems, max_depth=15)


if __name__ == "__main__":
    run()