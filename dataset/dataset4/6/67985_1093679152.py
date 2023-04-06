import locale
import threading

def thread():
    print("thread locale:", locale.getlocale())

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
#locale.getlocale()

t = threading.Thread(target=thread)
t.start()
t.join()