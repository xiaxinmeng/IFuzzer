from mock import patch

import flask


def some_function():
    flask.g.somevariable = True
    return flask.g.somevariable