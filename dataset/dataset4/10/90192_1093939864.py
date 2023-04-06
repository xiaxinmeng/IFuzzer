class Greeting():
    pass

def new_init(inst, name):
    inst.text = f"Hello, {name}\n"

Greeting.__init__ = new_init

Greeting("Miro")