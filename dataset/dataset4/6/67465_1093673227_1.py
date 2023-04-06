from PyQt5.QtMultimedia import QMediaPlaylist

class MyMeta(type(QMediaPlaylist)):
    def __setattr__(cls, key, value):
        print("OK")