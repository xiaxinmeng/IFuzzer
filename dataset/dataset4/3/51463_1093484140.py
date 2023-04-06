class Target(object):
    def start(self, tag, attrib):
        print('i see start', tag)
    def end(self, tag):
        print('i see end', tag)
    def close(self):
        return "DONE"

parser = ET.XMLParser(target=Target())
parser.feed("<TAG>sd</TAG>")