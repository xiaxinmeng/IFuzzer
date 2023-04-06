import email
with open('msg_01.txt', 'rb') as fp:
    msg = email.parser.BytesParser().parse(fp)
print(msg.get('Message-ID'))