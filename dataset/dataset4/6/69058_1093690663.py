# Decode binary data
x = data.decode('ascii', 'surrogateescape')
# %-format query
psql = sql % (escape(x),)  # sql is unicode
# Encode sql to connection encoding (latin1 or utf8)
query_bytes = psql.encode('utf-8', 'surrogateescape')