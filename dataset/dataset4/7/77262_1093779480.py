import multiprocessing
import json


def process(data):
    with open('/tmp/fd/%d.json' % data['name'], 'w') as f:
        f.write(json.dumps(data))
    return 'processed %d' % data['name']

if __name__ == '__main__':
    pool = multiprocessing.Pool(1000)
    try:
        for _ in range(10000000):
            x = {'name': _}
            pool.apply(process, args=(x,))
    finally:
        pool.close()
        del pool