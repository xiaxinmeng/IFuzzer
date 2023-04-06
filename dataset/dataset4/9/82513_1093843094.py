import email
import email.policy

text = "Subject: =?us-ascii?X?somevalue?="
eml = email.message_from_string(text, policy=email.policy.default)
eml.get('Subject')