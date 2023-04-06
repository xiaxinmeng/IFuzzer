from opcode import *
code = bytes(
    chr(opmap["JUMP_FORWARD"]) + chr(0) + chr(0) +
    chr(EXTENDED_ARG) + chr(1) + chr(0) +
    chr(opmap["JUMP_FORWARD"]) + chr(0) + chr(0) +
    chr(opmap["RETURN_VALUE"]),
    encoding="latin-1"
)
import dis
dis.dis(code)
print(dis.findlabels(code))
if dis.findlabels(code) == [0x0000+3, 0x00010000+9]:
    print("Test passed")