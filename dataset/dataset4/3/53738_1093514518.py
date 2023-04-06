for key,value in re.finditer(r'(\w+):(\w+)', text):
  data[key] = value