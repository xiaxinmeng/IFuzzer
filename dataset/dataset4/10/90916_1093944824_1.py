expected_opinfo_outer = [Instruction(opname, opcode, arg, argval, argrepr,
                                     offset, starts_line, is_jumps_target)
    for opname, opcode, arg, argval, argrepr, offset, starts_line, is_jumps_target in
(('LOAD_CONST', 100,    1,   3,     '3',      0,      2,           False),
 ('LOAD_CONST', 100,    2,   4,     '4',      3,      None,        False),
 ...
)]