import re
RE_C_COMMENTS    = re.compile(r"/\*(.|\s)*?\*/", re.MULTILINE|re.DOTALL|re.UNICODE)
text = "Special section /* valves:\n\n\nsilicone\n\n\n\n\n\n\nHarness:\n\n\nmetal and plastic fibre\n\n\n\n\n\n\nInner frame:\n\n\nmultibutylene\n\n\n\n\n\n\nWeight:\n\n\n147 g\n\n\n\n\n\n\n\n\n\n\n\n\n\nSelection guide\n"