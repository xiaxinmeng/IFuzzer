import unittest
from xml.etree import ElementTree as ET

class Target(object):
    def start(self, tag, attrib):
        raise ValueError("raise start")

    def end(self, tag):
        raise ValueError("raise end")

    def close(self):
        raise ValueError("raise close")

parser = ET.XMLParser(target=Target())
parser.feed("<root><test /></root>")