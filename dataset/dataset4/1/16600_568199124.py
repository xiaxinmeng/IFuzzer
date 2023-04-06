import functools, inspect

class Dog:
    async def abark(self): pass

inspect.iscoroutinefunction(dog.abark)  # True
inspect.iscoroutinefunction(functools.partial(dog.abark))  # False (should probably be True?)