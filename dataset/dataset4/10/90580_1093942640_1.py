for instr in dis.Bytecode(source):
    if instr.positions:
        lineno = instr.positions[0]
    else:
        lineno = None
    print("located in: ", lineno)