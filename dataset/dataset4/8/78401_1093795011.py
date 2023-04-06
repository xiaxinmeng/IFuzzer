import email.generator
import email.policy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from unittest import TestCase


def create_message(subject, sender, recipients, body):
    msg = MIMEMultipart()
    msg.set_charset('utf-8')
    msg.policy = email.policy.SMTP
    msg.attach(MIMEText(body, 'html'))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(recipients)
    return msg

class TestEmailMessage(TestCase):
    def _make_message(self, subject):
        return create_message(
            subject=subject, sender='me@site.com',
            recipients=['me@site.com'], body='Some text',
        )

    def test_ascii_message_no_len_limit(self):
        # very long subject consisting of a single word
        subject = 'Q' * 100
        msg = self._make_message(subject)
        self.assertTrue(str(msg))

    def test_non_ascii_message_no_len_limit(self):
        # very long subject consisting of a single word
        subject = 'Ц' * 100
        msg = self._make_message(subject)
        self.assertTrue(str(msg))