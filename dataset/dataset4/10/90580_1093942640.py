for instr in dis.Bytecode(source):
    print("located in: ", instr.positions.lineno)