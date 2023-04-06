import multiprocessing, sqlite3
def hang():
   sqlite3.connect('/tmp/foo')
if __name__ == '__main__':
   multiprocessing.Pool(2).apply_async(hang, []).get(999)
print('done')