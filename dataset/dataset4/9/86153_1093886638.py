from __future__ import annotations
from functools import singledispatchmethod


class Comparable:
    @singledispatchmethod
    def compare(self, arg: object):
        raise NotImplementedError("what")

    @compare.register
    def _(self, arg: Comparable):
        return "somewhat similar"