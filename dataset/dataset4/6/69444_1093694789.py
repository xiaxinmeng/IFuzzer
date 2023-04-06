
class HeaderBugWorkaround(email.header.Header):
    def encode(self, splitchars=' ', **kwargs):  # only split on spaces, rather than splitchars=';, '
        return email.header.Header.encode(self, splitchars, **kwargs)

# and then...

msg['Subject'] = HeaderBugWorkaround(subject, 'utf-8', header_name='Subject')

