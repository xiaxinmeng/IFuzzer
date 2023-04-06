if (event.state & 12) != 0 and event.keysym == "Home":
    # state&1==shift, state&4==control, state&8==alt
    return # <Modifier-Home>; fall back to class binding