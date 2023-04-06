async def do_thing():
   someobj.a =1
   await do_io_setattr(someobj, "b", 2)