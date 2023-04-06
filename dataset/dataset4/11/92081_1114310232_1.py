
msg = EmailMessage()
msg.policy = msg.policy.clone(max_line_length=sys.maxsize)
