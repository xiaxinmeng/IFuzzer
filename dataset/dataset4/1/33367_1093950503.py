import re
wpat = re.compile(r'(?<!self\.)\b([A-Za-z_]\w*)\s*\(')
m = wpat.search('   a(')