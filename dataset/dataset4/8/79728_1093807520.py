import re
from email.policy import EmailPolicy

class UnfoldingEncodedStringHeaderPolicy(EmailPolicy):
    def header_fetch_parse(self, name, value):
        # remove any leading whitespace from header lines
        # that separates apparent encoded-word token before further processing 
        # using somewhat crude CRLF-FWS-between-encoded-word matching
        value = re.sub(r'(?<=\?=)((?:\r\n|[\r\n])[\t ]+)(?==\?)', '', value)
        return super().header_fetch_parse(name, value)