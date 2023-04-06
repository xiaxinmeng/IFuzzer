co_positions = co_positions or iter(())

try:
  positions = next(co_positions)
except StopIteration:
  positions = None

Instruction(positions=positions)