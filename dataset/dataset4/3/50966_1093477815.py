g = {"X": 0, "Y": 0}

def goto_later(x, y): g["X"] = x; g["Y"] = y

def ontick():
    goto(g["X"], g["Y"])
    ontimer(ontick, 10)

ondrag(goto_later)
ontimer(ontick, 10)