def main():
    message = EmailMessage()
    message['From'] = 'no-reply@farmersbusinessnetwork.com'
    message['Reply-To'] = """MEGAN FOOOBAAAAAR <abcfghijkladbfrg@akdja.com>,"KDJEHGI, SCOTT KJUYT" <abcfghijkladbfrg@akdja.com>"""
    message['To'] = """"KDJEHGI, SCOTT KJUYT" <SCOTT.KDJEHGI@MYFNBBANK.COM>"""
    message['Subject'] = "does not matter"
    message['CC'] = """MEGAN FOOOBAAAAAR <abcfghijkladbfrg@akdja.com>,"KDJEHGI, SCOTT KJUYT" <abcfghijkladbfrg@akdja.com>"""
    message.set_content('foo bar')
    print(message.as_string())


if __name__ == '__main__':
    main()