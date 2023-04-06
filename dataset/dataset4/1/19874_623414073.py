class TestStringAnnotations(unittest.TestCase):
    def test_classvar(self):
        # Some expressions recognized as ClassVar really aren't.  But
        #  if you're using string annotations, it's not an exact
        #  science.
        # These tests assume that both "import typing" and "from
        # typing import *" have been run in this file.
        for typestr in ('ClassVar[int]',
                        'ClassVar [int]'
                        ' ClassVar [int]',
                        'ClassVar',
                        ' ClassVar ',
                        'typing.ClassVar[int]',
                        'typing.ClassVar[str]',
                        ' typing.ClassVar[str]',
                        'typing .ClassVar[str]',
                        'typing. ClassVar[str]',
                        'typing.ClassVar [str]',
                        'typing.ClassVar [ str]',

                        # Not syntactically valid, but these will
                        #  be treated as ClassVars.
                        'typing.ClassVar.[int]',
                        'typing.ClassVar+',
                        ):
            with self.subTest(typestr=typestr):
                @dataclass
                class C:
                    x: typestr

                # x is a ClassVar, so C() takes no args.
                C()

                # And it won't appear in the class's dict because it doesn't
                # have a default.
                self.assertNotIn('x', C.__dict__)

...