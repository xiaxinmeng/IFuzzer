C
g = _PyLong_GCD(a, b);
m = PyNumber_Multiply(g, a);
f = PyNumber_FloorDivide(a, m);
ab = PyNumber_Absolute(f);
return ab;
