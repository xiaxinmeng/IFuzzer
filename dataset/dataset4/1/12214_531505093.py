
Parser().parsestr("Content-Type: message/delivery-status\r\nInvalid line\r\n\r\n", headersonly=True).as_string()
