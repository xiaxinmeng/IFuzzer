def mgcd(a, *r):  # multiple gcd
  for b in r:
    while b:
      a, b = b, a % b
  return abs(a)