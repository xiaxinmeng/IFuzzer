class range:
    ...
    
    def __iter__(self):
        if self.inc_start:
            yield self.start
        
        i = self.start + self.step
        
        while i < self.stop if self.step > 0 else i > self.stop:
            yield i
            i += self.step
        
        if self.inc_stop and i == self.stop:
            yield i