import re
import fnmatch

urls = ['example/l1/l2/test3-1.py',
        'example/l1/test2-1.py',
        'example/l1/test2-2.py',
        'example/l1/l2/l3/test4-1.py']

regex = fnmatch.translate('example/*')
# 'example\\/.*\\Z(?ms)'
re.findall(regex, "\n".join(urls))
# return ['example/l1/l2/test3-1.py\nexample/l1/test2-1.py\nexample/l1/test2-2.py\nexample/l1/l2/l3/test4-1.py']