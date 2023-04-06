message = EmailMessage()
message["From"] = Address(addr_spec="bar@foo.com", display_name="Jens Troeger")
message["To"] = Address(addr_spec="foo@bar.com", display_name="Martín Córdoba")