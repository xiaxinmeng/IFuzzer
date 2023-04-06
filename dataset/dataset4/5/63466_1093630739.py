import logging
logging.root.addHandler(logging.FileHandler(filename='test.log',encoding='UTF16'))
logging.error( u'b\u0142\u0105d')