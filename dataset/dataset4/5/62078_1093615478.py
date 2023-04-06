encoded_data = 'abc'
for codecs in codecs.registered_codecs():
 decoded_data = codecs.decode(data)
 if decoded_data == 'cba': # cracked
  break