os.listdir(os.fsencode(strpath))
os.listdir(os.fsdecode(bytespath))
list(map(os.fsencode, os.listdir(strpath)))
list(map(os.fsdecode, os.listdir(bytespath)))