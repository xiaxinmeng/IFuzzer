if line.startswith(("import ", "import\t")):
    exec(line, {})
    continue