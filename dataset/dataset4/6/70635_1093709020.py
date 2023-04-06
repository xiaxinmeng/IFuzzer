from opcodes import *
import dis
bytecode = (
    chr(EXTENDED_ARG) + chr(1) + chr(0) + 
    chr(JUMP_IF_TRUE_OR_POP) + chr(0) + chr(0)
)
print(dis.findlabels(bytecode))