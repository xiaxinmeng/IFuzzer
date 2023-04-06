import os
try:
  from email.mime.multipart import MIMEMultipart
except ImportError:
  from email.MIMEMultipart import MIMEMultipart

m = MIMEMultipart('form-data')