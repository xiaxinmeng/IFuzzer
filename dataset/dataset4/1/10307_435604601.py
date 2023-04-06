import pydoc

def func123():
    # 124
    class class234:
        pass
    return class234

class class234:
    pass

if __name__ == "__main__":
    import inspect
    print(inspect.getcomments(func123()))
    print(pydoc.render_doc(func123()))