import base64
str = """GET http://www.google.com.hk/search?q=hotels+near+airport&pws=1&igu=1&ip=0.0.0.0&safe=images&gl=CN&gll=39.913889,116.391667&near=china&hl=zh-CN HTTP/1.0\nContent-Length: 0\nUser-Agent: Opera/9.80 (X11; Linux i686; U; en-US) Presto/2.9.173 Version/12.00\nProxy-Authorization: Basic\nAuthorization: Basic\nReferer: http://www.google.com/\n\n"""
base64.decodestring(str)