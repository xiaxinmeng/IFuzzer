# *** example.py begin ***
import types
import dis

# Create a test code object...
constants = [None] * (0x000129 + 1)
constants[0x000129] = "Hello world!"

code = types.CodeType(
    0,  # argcount
    0,  # posonlyargcount
    0,  # kwonlyargcount
    0,  # nlocals
    1,  # stacksize
    64,  # flags
    bytes([
        0x90, 0x01,  # EXTENDED_ARG 0x01
        0x09, 0xFF,  # NOP 0xFF
        0x90, 0x01,  # EXTENDED_ARG 0x01
        0x64, 0x29,  # LOAD_CONST 0x29
        0x53, 0x00,  # RETURN_VALUE 0x00
    ]),  # codestring=
    tuple(constants),  # constants
    (),  # names
    (),  # varnames
    '<no file>',  # filename
    'code',  # name
    1,  # firstlineno
    b''  # linetable
)

# ... and eval it to show that NOP resets EXTENDED_ARG
print("Output:", eval(code))

# Try to list all instructions via dis
print(list(dis.get_instructions(code)))