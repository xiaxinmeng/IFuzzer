import thread, time

class Frog:

    def __str__(self):
        return str(self)

f = Frog()
thread.start_new_thread(str,(f,))
time.sleep(1000)