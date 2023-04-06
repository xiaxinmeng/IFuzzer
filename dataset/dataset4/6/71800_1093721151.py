import json as json
import io

class EmptyIterator(list):
    def __iter__(self):
        while False:
            yield 1
    def __len__(self):
        return 1

def dump_to_str(data):
    return json.dumps(data)

def dump_to_file(data):
    stream = io.StringIO()
    json.dump(data, stream)
    return stream.getvalue()


data = {'it': EmptyIterator()}
print('to str: {0}'.format(dump_to_str(data)))
print('to file: {0}'.format(dump_to_file(data)))