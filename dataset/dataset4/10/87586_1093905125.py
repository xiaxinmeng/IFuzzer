from math import gcd
from fractions import Fraction
import operator
import math

class Henrici(Fraction):
    'Reformulate _mul to reduce the size of intermediate products'