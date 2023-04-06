print('Top of Module')
class C:
    def f(s): print('Method C.f')

if __name__ == '__main__':
    print('Start of main block')
    import multiprocessing
    p = multiprocessing.Process(target=C.f, args=(C(),))
    p.start()
    p.join()