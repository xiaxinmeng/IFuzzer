CHUNK = ...
chunks = [''.join(map(quoter, bs[i:i+CHUNK]))
          for i in range(0, len(bs), CHUNK)]
return ''.join(chunks)