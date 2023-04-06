def replace_element(elem, replacement):
    '''replace the content of an ElementTree Element by that of
another
       one.
    '''
    elem.clear()
    elem.text = replacement.text
    elem.tail = replacement.tail
    elem.tag = replacement.tag
    elem.attrib = replacement.attrib
    try:
        elem[:] = replacement[:]  # works with Python 2.5 but not 3.1
    except AssertionError:
        del elem[:]
        for child in replacement:
            elem.append(child)