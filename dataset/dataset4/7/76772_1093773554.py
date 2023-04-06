import sys
async def f(): pass
sys.corocycle = [f]
sys.corocycle.append(sys.corocycle)