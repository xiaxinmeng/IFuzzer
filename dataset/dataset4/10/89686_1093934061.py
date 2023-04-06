# writing 5 chunks of length 10
for i in range(5):
    text = str(i+1) * 10  # concatenate 10 chars
    chunk = '{0:d}\r\n'.format(len(text)) + text + '\r\n'
    self.wfile.write(chunk.encode(encoding='utf-8'))

# writing close sequence
close_chunk = '0\r\n\r\n'
self.wfile.write(close_chunk.encode(encoding='utf-8'))