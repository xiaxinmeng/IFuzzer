
import textwrap

def get_something_string():
    return textwrap.dedent("""\
        test text2
        test text3
        test text4""")

textwrap.dedent(f"""\
    test text1
    {get_something_string()}
    test text5
    test text6""")
