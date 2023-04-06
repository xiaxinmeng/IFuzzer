
from email.utils import formataddr, parseaddr

identity = '"foo  bar" <foo@example.com>'

print(formataddr(parseaddr(identity)))
# 'foo  bar <foo@example.com>'

print(formataddr(parseaddr(formataddr(parseaddr(identity)))))
# 'foo bar <foo@example.com>'
