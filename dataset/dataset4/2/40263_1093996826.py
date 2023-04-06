def primes():
  yield 2
  for n in count(3):
    for p in primes():
      if p > sqrt(n):
        yield n
        break
      if n % p == 0:
        break