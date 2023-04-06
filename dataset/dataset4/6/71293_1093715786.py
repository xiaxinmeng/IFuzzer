
from wave import *
from configparser import *

cfg = ConfigParser()
cfg.read('appconfig.ini')
try:
  with Wave_read(cfg['samples']['sad_trombone']) as wav:
    n = wav.getnframes()
    frames = wav.readframes(n)
except Error as e:
  print("Invalid sample:", e)
except KeyError as e:
  print("Can't find {!r} in the config".format(str(e)))
else:
  play_sound(frames)
