import sys
import multiprocessing


def foo():
    return 'bar'


if __name__ == '__main__':
    proc = multiprocessing.Process(target=foo)
    proc.start()
    proc.join()
    with open('process_exit_code.txt', 'w') as f:
        f.write(sys.version)
        f.write('\nprocess exit code: ')
        f.write(str(proc.exitcode))