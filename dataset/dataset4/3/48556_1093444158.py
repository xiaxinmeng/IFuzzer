def main():
    # coding: utf8
    ADDRESS = 'victor.stinner@haypocalc.com'
    from email.mime.text import MIMEText
    msg = MIMEText('accent éôŁ', 'plain', 'utf-8')
    msg['Subject'] = 'sujet éôł'
    msg['From'] = ADDRESS
    msg['To'] = ADDRESS
    text = msg.as_string()
    print("--- FLATTEN ---")
    print(text)
    return
    import smtplib
    client=smtplib.SMTP('smtp.free.fr')
    client.sendmail(ADDRESS, ADDRESS, text)
    client.quit()
main()