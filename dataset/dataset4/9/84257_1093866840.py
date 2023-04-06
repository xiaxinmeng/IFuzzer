for i in range(1,10000000):
     timestamp=datetime.datetime.utcnow().isoformat()
     if len(timestamp)!=26:
         print(timestamp)