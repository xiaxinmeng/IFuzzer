def test_wav(h, f):
     import wave
     # 'RIFF' <len> 'WAVE' 'fmt ' <len>
     if h[:4] != 'RIFF' or h[8:12] != 'WAVE' or h[12:16] != 'fmt ':
         return None
     f.seek(0)
     try:
         w = wave.openfp(f, 'r')
     except (EOFError, wave.Error):
         return None
     return ('wav', w.getframerate(), w.getnchannels(), \
             w.getnframes(), 8*w.getsampwidth())