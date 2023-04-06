from multiprocessing import Process,Manager

def f(d):
    d['1'] = '1'
    d['2']['1'] = 'Try To Write'

if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()