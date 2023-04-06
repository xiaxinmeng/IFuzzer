class B:
    def close(self):
        pass
    
async with closing(B()):
    pass