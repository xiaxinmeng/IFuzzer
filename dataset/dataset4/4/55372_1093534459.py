with open(name) as fp:
  for line in fp:
    if line == sentinel:
      break
    process(line)