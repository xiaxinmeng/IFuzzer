from email.header import Header

def main():
    # coding: utf8
    ADDRESS = 'victor.stinner@haypocalc.com'
    from email.mime.text import MIMEText
    msg = MIMEText('accent \xe9\xf4\u0142', 'plain', 'utf-8')
    msg['Subject'] = Header('sujet \xe9\xf4\u0142'.encode('utf-8'),
                            'utf-8')
    msg['From'] = ADDRESS
    msg['To'] = ADDRESS
    text = msg.as_string()
    print("--- FLATTEN ---")
    print(text)
    return

main()