import json

def map_gen():
    headers = "head1,head2,head3"
    items = "item1,item2,item3"
    record = dict(zip(headers.split(','), items.split(',')))
    yield (headers, str(record))

def reduce_gen():
    for line in map_gen():
        yield ("[" + ",".join(line) + "]")

if __name__=="__main__":
    for item in reduce_gen():
        json.loads(json.dumps(item))