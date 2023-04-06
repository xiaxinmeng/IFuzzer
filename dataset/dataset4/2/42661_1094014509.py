import wave
import os

f = os.popen('madplay -o wave:- foo.mp3')
wf = wave.open(f, 'rb')