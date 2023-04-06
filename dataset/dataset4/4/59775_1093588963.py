import email.header
print(email.header.decode_header("foo =?windows-1251?Q?bar?="))