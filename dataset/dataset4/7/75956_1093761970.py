stdin = sys.stdin
sys.stdin = open(0, "r", buffering=0, encoding=stdin.encoding, errors=stdin.errors, newline=stdin.newline)