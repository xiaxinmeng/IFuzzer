from email.parser import BytesFeedParser
import email.policy

def main():
    eml_string = 'From: Nobody <""@example.org>'
    parser = BytesFeedParser(policy = email.policy.default)
    parser.feed(eml_string.encode())
    msg = parser.close()
    print(msg.get('From').addresses[0].addr_spec)
    print(repr(msg.get('From')._parse_tree))
    print(msg.as_string())