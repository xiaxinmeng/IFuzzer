def func123():
    class class234:
        def func(self):
            pass
    return class234

class class345:
    def func456(self):
        class class567:
            pass
        return class567

if __name__ == "__main__":
    import inspect
    print(inspect.getsource(func123()))
    print(inspect.getsource(class345().func456()))