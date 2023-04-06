#!/usr/bin/env python
import sys
import wave
w = wave.open(sys.stdout, 'w')
w.setnchannels(1)
w.setsampwidth(1)
w.setframerate(32000)
w.setnframes(0)
w.close()