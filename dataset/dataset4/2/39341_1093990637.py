import email
import sys

msg = email.message_from_file(sys.stdin)
sys.stdout.write(msg.as_string())