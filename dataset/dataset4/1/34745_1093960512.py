#!/usr/bin/env python
#
from Numeric import *
from math import *
import random

N=1000

sigma=fromfunction(lambda
x:random.uniform(0.1,3.0),range(N))