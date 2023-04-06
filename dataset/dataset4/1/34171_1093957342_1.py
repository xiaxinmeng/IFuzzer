self.lock.acquire() 
try: 
    ... 
finally: 
    self.lock.release() 