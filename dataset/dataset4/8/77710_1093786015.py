import email.policy
policy = email.policy.default.clone(max_line_length=20)
actual = policy.fold('Subject', '\u0105' * 12)