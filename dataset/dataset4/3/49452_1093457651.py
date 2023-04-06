#!/usr/bin/env python
import sys
import wave
w = wave.open(sys.stdout, 'w')
w.setnchannels(1)
w.setsampwidth(1)
w.setframerate(2000)
w.setnframes(100)
for _ in range(50): w.writeframesraw('\x00\xff')
w.close()