import readline
def myinput(prompt, initial=''):
    readline.set_startup_hook(lambda: readline.insert_text(initial))
    try:
        response = input(prompt)
    finally:
        readline.set_startup_hook(None)
    return response