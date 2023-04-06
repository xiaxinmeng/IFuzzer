import re
from email.policy import EmailPolicy

class UnfoldingHeaderEmailPolicy(EmailPolicy):
    def header_fetch_parse(self, name, value):
        # remove any leading whitespace from header lines
        # before further processing
        value = re.sub(r'(?<=[\n\r])([\t ])', '', value)
        return super().header_fetch_parse(name, value)

custom_policy = UnfoldingHeaderEmailPolicy()