class A:
    async def close(self):
        pass
    
with closing(A()):
    pass