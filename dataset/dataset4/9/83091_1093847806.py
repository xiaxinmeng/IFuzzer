
from io import StringIO, BytesIO
from lxml import etree
import os
import readline

HOME = os.path.expanduser("~")

ofile = HOME + '/data/2web/reagle.org/joseph/plan/plans/index.html'
plan_fd = open(ofile, 'r', encoding='utf-8', errors='replace')
plan_content = plan_fd.read()
plan_fd.close()
plan_tree = etree.parse(StringIO(plan_content),
                        etree.XMLParser(ns_clean=True, recover=True))
ul_found = plan_tree.xpath(
    '''//x:div[@id='Done']/x:ul''',
    namespaces={'x': 'http://www.w3.org/1999/xhtml'})
