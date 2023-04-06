variable = 'text'

def changeVariable():
    global variable
    exec("variable = 'newText'")

changeVariable()

print(str(variable))