import threading
import time

def threadFunc():
    while True:
        print('new thread')
        time.sleep(2)
def main():
    th = threading.Thread(target=threadFunc())
    th.start()
    while True:
       print('main Thread')
       time.sleep(1)
    th.join()
 
if __name__ == '__main__':
   main()