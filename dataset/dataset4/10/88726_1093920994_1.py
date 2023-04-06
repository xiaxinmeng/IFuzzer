
from email import header, charset

h = header.make_header([(str("中文").encode("gb2312"),
                         charset.Charset("gb2312"))])
print(h.encode())
