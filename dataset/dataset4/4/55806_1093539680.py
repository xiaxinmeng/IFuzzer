import configparser
import codecs

cfg = configparser.ConfigParser()
cfg.write(codecs.open('filename','wb+','utf-8'))