import re
s = "hello"
s = re.sub(re.escape(r'(\d+?)'), '(?:\d+?)', s)