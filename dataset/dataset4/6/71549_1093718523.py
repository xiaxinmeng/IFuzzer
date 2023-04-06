import json


class ObjectCounter:

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __json__(self):
       return '[{name}] {count}'.format(name=self.name, count=self.count)


object_counter = ObjectCounter('DC1', 3789)
my_json_string = json.dumps({'success': True, 'counter': object_counter})