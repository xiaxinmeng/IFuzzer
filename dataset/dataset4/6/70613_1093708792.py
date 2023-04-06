from email.headerregistry import Address
...
msg['From'] = Address("Pepé Le Pew", "pepe@example.com")
msg['To'] = (Address("Penelope Pussycat", "penelope@example.com"),
             Address("Fabrette Pussycat", "fabrette@example.com"))