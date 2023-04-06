
import asyncio

class HevonPaskaa:
    
    def __init__(self):
        pass
        
    async def goodfunc(self):
        await asyncio.sleep(3)
        print("Good function was called allright")
        print("While it was sleeping, hevonpaska must have been executed")

    async def hevonpaska(self):
        """When this cofunction is scheduled as a task:
        - The NameError is not raised immediately .. !
        - BaseException is raised immeadiately OK
        """
        raise NameError # WARNING: This is catched only when the program terminates
        # raise BaseException # WARNING: comment the previous line and uncomment this: this is catched immediately

    async def cofunc2(self):
        # # we'd like this to raise the NameError immediately:
        self.task = asyncio.get_event_loop().create_task(self.hevonpaska())
        self.good_task = asyncio.get_event_loop().create_task(self.goodfunc())
        # # this raises NameError immediately because the task is garbage collected:
        # self.task = None
        
    async def cofunc1(self):
        await self.cofunc2()
        print("\nwaitin' : where-t-f is the NameError hiding!?")
        await asyncio.sleep(6)
        print("Wait is over, let's exit\n")

hv = HevonPaskaa()

asyncio.get_event_loop().run_until_complete(hv.cofunc1())
