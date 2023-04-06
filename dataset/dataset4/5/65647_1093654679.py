import email.parser
import time
data = 'From: example@example.com\n\n' + 'x' * 10000000
start = time.time()
email.parser.Parser().parsestr(data)
print(time.time() - start)