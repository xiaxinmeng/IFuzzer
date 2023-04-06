from io import StringIO
import pydoc
import sys


if __name__ == '__main__':
    help_text = StringIO()

    helper = pydoc.Helper(output=help_text)
    # help contents are written to help_text as expected
    helper.help('pydoc')

    # the following calls each show the help contents in a pager instead
    # of using the configured output
    helper.help('True')
    helper.help('False')
    helper.help('None')
    helper.help('**')  # symbol example
    helper.help('SEQUENCES')  # topic example
    helper.help('await')  # keyword example