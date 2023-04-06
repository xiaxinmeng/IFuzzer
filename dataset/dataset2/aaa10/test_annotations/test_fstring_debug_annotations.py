import unittest
import sys
from textwrap import dedent
import test_annotations

def test_fstring_debug_annotations():
    PostponedAnnotationsTestCase.assertAnnotationEqual("f'{x=!r}'", expected="f'x={x!r}'")
    PostponedAnnotationsTestCase.assertAnnotationEqual("f'{x=:}'", expected="f'x={x:}'")
    PostponedAnnotationsTestCase.assertAnnotationEqual("f'{x=:.2f}'", expected="f'x={x:.2f}'")
    PostponedAnnotationsTestCase.assertAnnotationEqual("f'{x=!r}'", expected="f'x={x!r}'")
    PostponedAnnotationsTestCase.assertAnnotationEqual("f'{x=!a}'", expected="f'x={x!a}'")
    PostponedAnnotationsTestCase.assertAnnotationEqual("f'{x=!s:*^20}'", expected="f'x={x!s:*^20}'")

PostponedAnnotationsTestCase = test_annotations.PostponedAnnotationsTestCase()
test_fstring_debug_annotations()
