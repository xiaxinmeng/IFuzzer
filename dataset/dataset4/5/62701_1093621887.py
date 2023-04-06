import unittest
from xml.etree import ElementTree as ET

class Target(object):
    def start(self, tag, attrib):
        print("start")
        raise ValueError("raise start")

    def end(self, tag):
        print("end")
        raise ValueError("raise end")

    def close(self):
        print("close")
        raise ValueError("raise close")

parser = ET.XMLParser(target=Target())
parser.feed("<root><test /></root>")