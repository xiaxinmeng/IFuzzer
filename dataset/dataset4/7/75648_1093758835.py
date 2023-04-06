import xml.etree.ElementTree as ET    # WORKS
import xml.etree.cElementTree as ET    # DOES NOT WORK
import multiprocessing

tree = ET.parse('country_data.xml')
root = tree.getroot()

manager = multiprocessing.Manager()
elems_saved = manager.dict()