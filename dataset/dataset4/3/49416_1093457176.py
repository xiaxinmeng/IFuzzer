def escape_xml_illegal_chars(unicodeString, replaceWith=u'?'):
	return re.sub(u'[\x00-\x08\x0b\x0c\x0e-\x1F\uD800-\uDFFF\uFFFE\uFFFF]', replaceWith, unicodeString)