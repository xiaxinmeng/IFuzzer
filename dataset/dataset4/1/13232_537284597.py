
def for_global_before():
    global bar
    for bar in []:
        ...

def for_global_after():
    for bar in []:
        ...
    global bar

for_global_before()
for_global_after()

# ----

def class_global_before():
    global bar
    class bar:
        ...

def class_global_after():
    class bar:
        ...
    global bar

class_global_before()
class_global_after()

# ----

def def_global_before():
    global bar
    def bar():
        ...

def def_global_after():
    def bar():
        ...
    global bar

def_global_before()
def_global_after()
