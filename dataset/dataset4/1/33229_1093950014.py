import re
p=re.compile('(?<!abc)(def)')
p.search('abcddef')    