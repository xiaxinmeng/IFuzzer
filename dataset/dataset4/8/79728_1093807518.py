# crude CRLF-FWS-between-encoded-word matching
value = re.sub(r'(?<=\?=(\r\n|\n|\r))([\t ]+)(?==\?)', '', value)