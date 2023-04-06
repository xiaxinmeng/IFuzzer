import email.policy
message=email.message_from_string("Message-id: <A@", policy=email.policy.default)
message['Message-id']