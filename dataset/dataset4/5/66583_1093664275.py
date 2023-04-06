old_stdin = sys.stdin
try:
  sys.stdin = mock_input
  ...
finally:
  sys.stdin = old_stdin