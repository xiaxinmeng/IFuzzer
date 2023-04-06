class GraphvizResult(NamedTuple):
    svg: str
    err: str

def create_svg(dot: str) -> GraphvizResult:
    'Convert a string in the "dot" format to an "svg" string using Graphviz'
    cp = run(['dot', '-Tsvg'], input=dot, capture_output=True, text=True)
    result = cp.stdout
    if not cp.returncode:
        i = result.index('<svg ')
        result = result[i:]
    return GraphvizResult(result, cp.stderr)

def create_svg(dot: str) -> GraphvizResult:
    'Convert a string in the "dot" format to an "svg" string using Graphviz'
    cp = run(['dot', '-Tsvg'], input=dot, capture_output=True, text=True)
    result = cp.stdout
    if cp:
        i = result.index('<svg ')
        result = result[i:]
    return GraphvizResult(result, cp.stderr)