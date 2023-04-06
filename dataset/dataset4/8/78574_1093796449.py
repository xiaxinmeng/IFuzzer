import datalab.storage as storage
storage.Bucket('mybucket').item(path).write_to(json.dumps(response), 'application/json')