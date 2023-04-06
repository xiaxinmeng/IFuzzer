if line.startswith(("import ", "import\t")):
    exec(line, globals().copy())
    continue