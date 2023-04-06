def trace(frame, event, args):
  frame.f_trace_opcodes = True
  if event == 'opcode':
    disassemble(frame.f_code, frame.f_lasti)
  return frame