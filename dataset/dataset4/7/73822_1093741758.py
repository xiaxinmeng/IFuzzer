
def parse_indent(indent):
    """Parse the argparse indent argument."""
    if indent == 'None':
        return None
    if indent == r'\t':
        return '\t'
    try:
        return int(indent)
    except ValueError:
        return indent
