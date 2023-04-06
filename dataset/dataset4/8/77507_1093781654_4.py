hasjrel = set(Opcode(x) for x in opcode.hasjrel)
hasjabs = set(Opcode(x) for x in opcode.hasjabs)
hasjump = hasjrel.union(hasjabs)