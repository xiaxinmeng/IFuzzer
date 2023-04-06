from xml.etree.ElementTree import _escape_cdata ,_raise_serialization_error
from mock import patch

def _escape_cdata(text):
    # escape character data
    try:
        # it's worth avoiding do-nothing calls for strings that are
        # shorter than 500 character, or so.  assume that's, by far,
        # the most common case in most applications.
        if "&" in text:
            text = text.replace("&", "&amp;")
        if "<" in text:
            text = text.replace("<", "&lt;")
        if ">" in text:
            text = text.replace(">", "&gt;")
        if "'" in text:
            text = text.replace("'", "&apos;")
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)

from xml.etree import cElementTree as ET