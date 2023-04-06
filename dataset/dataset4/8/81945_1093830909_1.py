eml = email.message_from_string(text, policy=email.policy.SMTPUTF8)
eml.as_string()